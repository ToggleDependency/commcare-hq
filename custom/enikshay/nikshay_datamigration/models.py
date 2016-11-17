from django.db import models


class PatientDetail(models.Model):
    PregId = models.CharField(max_length=255, primary_key=True) # need to remove trailing whitespace in Excel
    scode = models.CharField(max_length=255, null=True, default='default')
    Dtocode = models.CharField(max_length=255, null=True)
    Tbunitcode = models.CharField(max_length=255, null=True)
    pname = models.CharField(max_length=255, null=True)
    pgender = models.CharField(max_length=255, null=True)
    page = models.CharField(max_length=255, null=True)
    poccupation = models.CharField(max_length=255, null=True)
    paadharno = models.CharField(max_length=255, null=True) # big ints (scientific notation) and nulls. requires some formatting
    paddress = models.CharField(max_length=255, null=True)
    pmob = models.CharField(max_length=255, null=True)  # contains " ", big ints
    plandline = models.CharField(max_length=255, null=True)
    ptbyr = models.CharField(max_length=255, null=True)  # dates, but not clean
    pregdate1 = models.CharField(max_length=255, null=True)  # remove time in Excel (format as DD-MM-YYYY)
    cname = models.CharField(max_length=255, null=True)
    caddress = models.CharField(max_length=255, null=True)
    cmob = models.CharField(max_length=255, null=True)  # contains "  ", big ints
    clandline = models.CharField(max_length=255, null=True)
    cvisitedby = models.CharField(max_length=255, null=True)
    cvisitedDate1 = models.CharField(max_length=255, null=True)  # datetimes, look like they're all midnight
    dcpulmunory = models.CharField(
        max_length=255, choices=(
            ('y', 'y'),
            ('N', 'N'),
        ), null=True
    )  # y or N
    dcexpulmunory = models.CharField(max_length=255, null=True)
    dcpulmunorydet = models.CharField(max_length=255, null=True)
    dotname = models.CharField(max_length=255, null=True)
    dotdesignation = models.CharField(max_length=255, null=True)
    dotmob = models.CharField(max_length=255, null=True)
    dotlandline = models.CharField(max_length=255, null=True)
    dotpType = models.CharField(max_length=255, null=True)
    dotcenter = models.CharField(max_length=255, null=True)
    PHI = models.CharField(max_length=255, null=True)
    dotmoname = models.CharField(max_length=255, null=True)
    dotmosignDate = models.CharField(max_length=255, null=True)  # datetimes, look like they're all midnight. also have a bunch of 1/1/1990
    atbtreatment = models.CharField(max_length=255, choices=(
        ('Y', 'Y'),
        ('N', 'N'),
    ), null=True)  # Y or N
    atbduration = models.CharField(max_length=255, null=True)  # some int, some # months poorly formatted
    atbsource = models.CharField(max_length=255, null=True, choices=(
        ('G', 'G'),
        ('O', 'O'),
        ('P', 'P'),
    ))
    atbregimen = models.CharField(max_length=255, null=True)
    atbyr = models.CharField(max_length=255, null=True)
    Ptype = models.CharField(max_length=255, null=True)
    pcategory = models.CharField(max_length=255, null=True)
    InitiationDate1 = models.CharField(max_length=255, null=True)  # datetimes, look like they're all midnight

    @property
    def first_name(self):
        return self._list_of_names[0]

    @property
    def middle_name(self):
        return ' '.join(self._list_of_names[1:-1])

    @property
    def last_name(self):
        return self._list_of_names[-1]

    @property
    def _list_of_names(self):
        return self.pname.split(' ')

    @property
    def sex(self):
        return {
            'F': 'female',
            'M': 'male',
            'T': 'transgender'
        }[self.pgender]


class Outcome(models.Model):
    PatientId = models.ForeignKey(PatientDetail, primary_key=True)
    Outcome = models.CharField(max_length=255, null=True)
    OutcomeDate1 = models.CharField(max_length=255, null=True)
    MO = models.CharField(max_length=255, null=True)
    XrayEPTests = models.CharField(max_length=255, null=True)
    MORemark = models.CharField(max_length=255, null=True)
    HIVStatus = models.CharField(max_length=255, null=True)
    HIVTestDate = models.CharField(max_length=255, null=True)
    CPTDeliverDate = models.CharField(max_length=255, null=True)
    ARTCentreDate = models.CharField(max_length=255, null=True)
    InitiatedOnART = models.CharField(max_length=255, null=True)
    InitiatedDate = models.CharField(max_length=255, null=True)


class Followup(models.Model):
    PatientID = models.ForeignKey(PatientDetail)  # requires trimming whitespace in excel and moving to end of CSV
    IntervalId = models.CharField(max_length=255, null=True)
    TestDate = models.CharField(max_length=255, null=True)
    DMC = models.CharField(max_length=255, null=True)
    LabNo = models.CharField(max_length=255, null=True)
    SmearResult = models.CharField(max_length=255, null=True)
    PatientWeight = models.CharField(max_length=255, null=True)


class Household(models.Model):
    PatientID = models.ForeignKey(PatientDetail)  # have to move to end of excel CSV
    Name = models.CharField(max_length=255, null=True)
    Dosage = models.CharField(max_length=255, null=True)
    Weight = models.CharField(max_length=255, null=True)
    M1 = models.CharField(max_length=255, null=True)
    M2 = models.CharField(max_length=255, null=True)
    M3 = models.CharField(max_length=255, null=True)
    M4 = models.CharField(max_length=255, null=True)
    M5 = models.CharField(max_length=255, null=True)
    M6 = models.CharField(max_length=255, null=True)
