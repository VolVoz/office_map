from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta(object):
        abstract = True


class Employee(BaseModel):
    email = models.EmailField(max_length=70, blank=True, unique=True)


class Room(BaseModel):
    employees_count = models.IntegerField(null=True)
    members = models.ManyToManyField(Employee, through='Office')


class Office(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
