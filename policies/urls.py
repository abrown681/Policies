from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.policies_list, name='policies_list'),
]
