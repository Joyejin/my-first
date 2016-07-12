from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.sub_list, name='sub_list'),
]
