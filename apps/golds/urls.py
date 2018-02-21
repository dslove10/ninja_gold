from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^process_money/farm$', views.farm),
	url(r'^process_money/cave$', views.cave),
	url(r'^process_money/house$', views.house),
	url(r'^process_money/casino$', views.casino)
]