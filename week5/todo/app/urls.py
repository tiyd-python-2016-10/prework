from django.conf.urls import url
from app.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^task/(?P<id>[0-9]*)', TaskView.as_view(), name="task_view"),
    url(r'^status/(?P<id>[0-9]*)', StatusView.as_view(), name="status_view"),
    url(r'^delete/(?P<id>[0-9]+)', delete, name="delete")
]
