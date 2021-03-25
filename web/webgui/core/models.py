# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SFibersStackCalibratorPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackCalibratorPar'
        verbose_name = 'SFibersStackDDLookupTable'
        verbose_name_plural = 'SFibersStackDDLookupTable'
        


class SFibersStackDDLookupTable(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackDDLookupTable'
        verbose_name = 'SFibersStackDDLookupTable'
        verbose_name_plural = 'SFibersStackDDLookupTable'


class SFibersStackDDUnpackerPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackDDUnpackerPar'
        verbose_name = 'SFibersStackDDUnpackerPar'
        verbose_name_plural = 'SFibersStackDDUnpackerPar'


class SFibersStackDigitizerPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackDigitizerPar'
        verbose_name = 'SFibersStackDigitizerPar'
        verbose_name_plural = 'SFibersStackDigitizerPar'


class SFibersStackGeomPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackGeomPar'
        verbose_name = 'SFibersStackGeomPar'
        verbose_name_plural = 'SFibersStackGeomPar'


class SFibersStackHitFinderFiberPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackHitFinderFiberPar'
        verbose_name = 'SFibersStackHitFinderFiberPar'
        verbose_name_plural = 'SFibersStackHitFinderFiberPar'


class SFibersStackHitFinderPar(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'SFibersStackHitFinderPar'
        verbose_name = 'SFibersStackHitFinderPar'
        verbose_name_plural = 'SFibersStackHitFinderPar'


class Configuration(models.Model):
    parameters = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    version = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('version', 'valid_from'),)
        db_table = 'configuration'
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'


class Files(models.Model):
    file_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    run_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('version', 'valid_from'),)
        db_table = 'files'
        unique_together = (('run_id', 'start_time', 'stop_time'),)
        verbose_name = 'Files'
        verbose_name_plural = 'Files'