from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import Room, Employee, Office
from .forms import EmployeeForm, RoomForm, OfficeForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse


class BaseInfoView(DetailView):
    def get(self, request, **kwargs):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'obj': obj})


class RoomInfo(BaseInfoView):
    model = Room
    form_class = RoomForm
    template_name = 'map/room_detail.html'


class EmployeeInfo(BaseInfoView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'map/employee_detail.html'


class BaseDeleteView(DeleteView):
    success_url = 'main'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        return reverse(self.success_url)


class RoomDelete(BaseDeleteView):
    model = Room
    template_name = "map/room_confirm_delete.html"

    def post(self, *args, **kwargs):
        room = self.get_object()
        if room.members.get_queryset():
            messages.add_message(self.request,
                                 messages.SUCCESS,
                                 'Can not delete the room where workers are!')
            return redirect(self.get_success_url())
        messages.add_message(self.request, messages.SUCCESS,
                             "The room has been successfully removed!")
        return self.delete(*args, **kwargs)


class EmployeeDelete(BaseDeleteView):
    model = Employee
    template_name = "map/employee_confirm_delete.html"

    def post(self, *args, **kwargs):
        if "remove_employee" in self.request.path:
            removable_user = self.get_object()
            removable_user.office_set.first().delete()
            messages.add_message(self.request,
                                 messages.SUCCESS,
                                 'An employee looking for another room :)')
            return redirect(self.get_success_url())
        return self.delete(*args, **kwargs)


class BaseUpdateView(UpdateView):
    success_url = 'main'
    template_name = 'map/map_edit.html'

    def get_object(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(BaseUpdateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        messages.add_message(self.request,
                             messages.SUCCESS, 'Object successfuly updated')
        return reverse(self.success_url)


class RoomUpdate(BaseUpdateView):
    model = Room
    form_class = RoomForm


class EmployeeUpdate(BaseUpdateView):
    model = Employee
    form_class = EmployeeForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        import pdb; pdb.set_trace()
        instance.save()
        return redirect(self.get_success_url())


class BaseCreateView(CreateView):
    success_url = 'main'
    template_name = 'map/map_edit.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, self.message)
        return reverse(self.success_url)


class EmployeeCreate(BaseCreateView):
    model = Employee
    form_class = EmployeeForm
    message = 'Employee successfuly updated'


class RoomCreate(BaseCreateView):
    model = Room
    form_class = RoomForm
    message = 'Room successfuly updated'


class OfficeCreate(BaseCreateView):
    model = Office
    form_class = OfficeForm
    message = 'Relationship successfuly updated'

    def form_valid(self, form):
        instance = form.save(commit=False)
        max_people = instance.room.employees_count
        employee = Employee.objects.get(email=instance.employee.email)
        if len(instance.room.members.get_queryset()) >= max_people:
            self.message = 'Sorry, this room is no more free places'
            return redirect(self.get_success_url())
        elif employee.office_set.get_queryset():
            self.message = 'Employee "{}":"{}", already in "{}" room!'.format(employee.name, employee.email, employee.office_set.get_queryset()[0].room.name)
            return redirect(self.get_success_url())
        instance.save()
        return redirect(self.get_success_url())


class MyView(View):
    def get(self, request):
        office = Room.objects.all()
        return render(request, 'map/office_map.html', {'office': office})
