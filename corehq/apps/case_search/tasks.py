from celery.task import task

from corehq.pillows.case_search import (
    CaseSearchReindexerFactory,
    delete_case_search_cases,
)


@task(serializer='pickle')
def reindex_case_search_for_domain(domain):
    CaseSearchReindexerFactory(domain=domain).build().reindex()


@task(serializer='pickle')
def delete_case_search_cases_for_domain(domain):
    delete_case_search_cases(domain)
