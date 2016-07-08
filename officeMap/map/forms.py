from django import forms
from .models import Employee, Room, Office


class EmployeeForm(forms.ModelForm):

    class Meta(object):
        model = Employee
        fields = ('name', 'email',)


class RoomForm(forms.ModelForm):

    class Meta(object):
        model = Room
        fields = ('name', 'employees_count',)


class OfficeForm(forms.ModelForm):

    class Meta(object):
        model = Office
        fields = ('employee', 'room',)
