from django.urls import path, include,re_path
from . import views

urlpatterns = [
	path('', views.index, name='dashboard'),
	re_path('^forms/',views.forms, name='forms'),
	re_path('^qty/',views.qtymasuk, name='qty'),
	re_path('^qty/(?P<id>\w+)',views.qtymasuk, name='qty'),
	re_path('^qty/',views.qtymasukForm, name='qty'),
]
