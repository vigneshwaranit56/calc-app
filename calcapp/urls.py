from django.conf.urls import url
from calcapp import views

urlpatterns = [
    url(r'^api/calculation$', views.operations_list),
    url(r'^api/calculation/(?P<pk>[0-9]+)$', views.operation_detail),
]