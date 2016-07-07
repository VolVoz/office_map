from django.test import TestCase
from map.models import Employee, Room, Office
import factory
from django.test import Client


class RoomFactory(factory.Factory):
    class Meta:
        model = Room

    name = 'Miting room'
    employees_count = 2


class RandomUserFactory(factory.Factory):
    class Meta:
        model = Employee

    name = factory.Faker('first_name')
    email = factory.Faker('email')


class EmployeeTestCase(TestCase):
    def setUp(self):
        self.employee = RandomUserFactory.create()
        self.rooom = RoomFactory.create()
        self.c = Client(enforce_csrf_checks=True)

    def test_get_create_employee_page(self):
        response = self.c.get('/new_employee/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'map/map_edit.html')

    def test_get_create_room_page(self):
        response = self.c.get('/new_room/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'map/map_edit.html')

    def test_get_create_office_page(self):
        response = self.c.get('/new_relationship/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'map/map_edit.html')

    #TODO: 302 0, errors with redirect, investigate a problem
