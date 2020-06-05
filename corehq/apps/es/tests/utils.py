import functools
import inspect
import json

from django.conf import settings
from django.test import override_settings
from importlib import reload


class ElasticTestMixin(object):

    def checkQuery(self, query, json_output, is_raw_query=False):
        if is_raw_query:
            raw_query = query
        else:
            raw_query = query.raw_query
        msg = "Expected Query:\n{}\nGenerated Query:\n{}".format(
            json.dumps(json_output, indent=4),
            json.dumps(raw_query, indent=4),
        )
        # NOTE: This method thinks [a, b, c] != [b, c, a]
        self.assertEqual(raw_query, json_output, msg=msg)


def reload_modules():
    from corehq.util.es import elasticsearch
    from corehq import elastic
    from corehq.util.es import interface
    from pillowtop import es_utils
    from pillowtop.processors import elastic as pelastic
    from corehq.util import elastic as uelastic
    reload(elasticsearch)
    reload(elastic)
    reload(interface)
    reload(es_utils)
    reload(pelastic)
    reload(uelastic)


def skip_and_reload_decorator(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        if not getattr(settings, 'ELASTICSEARCH_2_PORT', False):
            setattr(cls, '__unittest_skip__', True)
            setattr(cls, '__unittest_skip_why__', 'settings.ELASTICSEARCH_2_PORT is not defined')
            return cls
        builtins = ['setUp', 'setUpClass', 'tearDown', 'tearDownClass']
        for (method_name, method) in inspect.getmembers(cls):
            if method_name in builtins or method_name.startswith("test_"):
                setattr(cls, method_name, decorator(getattr(cls, method_name)))
        return cls
    return decorate


def reload_modules_decorator(fn):
    @functools.wraps(fn)
    def wrap(*args):
        with override_settings(ELASTICSEARCH_MAJOR_VERSION=2, ELASTICSEARCH_PORT=getattr('settings', 'ELASTICSEARCH_2_PORT', 5200)):
            reload_modules()
            res = fn(*args)
        reload_modules()
        return res
    return wrap


run_on_es2 = skip_and_reload_decorator(reload_modules_decorator)
