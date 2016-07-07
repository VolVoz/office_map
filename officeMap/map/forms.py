from django import forms
from .models import Employee, Room, Office


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'email',)


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'employees_count',)


class OfficeForm(forms.ModelForm):

    class Meta:
        model = Office
        fields = ('employee', 'room',)
