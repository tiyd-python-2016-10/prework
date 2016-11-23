from django.conf.urls import url
import app.views

urlpatterns = [
    url(r'^$', app.views.index_view, name="index")
]
