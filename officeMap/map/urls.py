from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MyView.as_view(), name='main'),
    url(r'^update_room/(?P<pk>[\w-]+)$', views.RoomUpdate.as_view(), name='update_room'),
    url(r'^update_employee/(?P<pk>[\w-]+)$', views.EmployeeUpdate.as_view(), name='update_employee'),
    url(r'^delete_room/(?P<pk>[\w-]+)$', views.RoomDelete.as_view(), name='delete_room'),
    url(r'^delete_employee/(?P<pk>[\w-]+)$', views.EmployeeDelete.as_view(), name='delete_employee'),
    url(r'^remove_employee/(?P<pk>[\w-]+)$', views.EmployeeDelete.as_view(), name='remove_employee'),
    url(r'^info_room/(?P<pk>[\w-]+)$', views.RoomInfo.as_view(), name='info_room'),
    url(r'^info_employee/(?P<pk>[\w-]+)$', views.EmployeeInfo.as_view(), name='info_employee'),
    url(r'^new_employee/$', views.EmployeeCreate.as_view(), name='new_employee'),
    url(r'^new_room/$', views.RoomCreate.as_view(), name='new_room'),
    url(r'^new_relationship/$', views.OfficeCreate.as_view(), name='new_relationship'),
]
