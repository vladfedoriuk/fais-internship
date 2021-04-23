from django.db import models

class Configuration(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    release = models.ForeignKey("Release",
                                on_delete=models.CASCADE,
                                related_name="%(class)s_versions")

    class Meta:
        abstract = True
        unique_together = (('version', 'valid_from'),)
        db_table = "configuration"
        
 
class Release(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return self.name
    
    class Meta:
        db_table = "Release"
        verbose_name = db_table
        verbose_name_plural = verbose_name       

class SFibersStackCalibratorPar(Configuration):
    class Meta:
        db_table = "SFibersStackCalibratorPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name

class SFibersStackDDLookupTable(Configuration):
    class Meta:
        db_table = "SFibersStackDDLookupTable"
        verbose_name = db_table
        verbose_name_plural = verbose_name


class SFibersStackDDUnpackerPar(Configuration):
    class Meta:
        db_table = "SFibersStackDDUnpackerPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name


class SFibersStackDigitizerPar(Configuration):
    class Meta:
        db_table = "SFibersStackDigitizerPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name
    

class SFibersStackGeomPar(Configuration):
    class Meta:
        db_table = "SFibersStackGeomPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name


class SFibersStackHitFinderFiberPar(Configuration):
    class Meta:
        db_table = "SFibersStackHitFinderFiberPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name


class SFibersStackHitFinderPar(Configuration):
    class Meta:
        db_table = "SFibersStackHitFinderPar"
        verbose_name = db_table
        verbose_name_plural = verbose_name


class Files(models.Model):
    file_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    run_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = (('run_id', 'start_time', 'stop_time'),)
        db_table = "files"
        verbose_name = db_table
        verbose_name_plural = verbose_name

       