# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Complex(models.Model):
    rowid = models.AutoField(primary_key=True, blank=True, null=False)
    complex_name = models.TextField(unique=True, null=False)
    street_address = models.TextField(null=False)
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_housing_complexes'


class Lease(models.Model):
    rowid = models.AutoField(primary_key=True, blank=True, null=False)
    resident = models.ForeignKey('Resident', models.DO_NOTHING)
    unit = models.ForeignKey('Unit', models.DO_NOTHING)
    lease_start = models.TextField()
    lease_end = models.TextField()
    created_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_leases'


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True, blank=True, null=False)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    email = models.TextField(unique=True, null=False)
    phone = models.TextField(unique=True, null=False)
    birthdate = models.TextField(null=False)
    gender = models.TextField(null=False)

    class Meta:
        managed = False
        db_table = 'tb_resident_info'

class Unit(models.Model):
    rowid = models.AutoField(primary_key=True, blank=True, null=False)
    complex = models.ForeignKey(Complex, models.DO_NOTHING)
    unit_number = models.TextField(null=False)
    gender = models.TextField()
    room = models.TextField()
    bed = models.TextField()
    room_type = models.TextField()
    rent_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_student_housing_units'
