from django.conf.urls import url
from django.contrib import admin

from property import views

urlpatterns = [
    url(r'^$', views.show_flats, name='main_page'),
    url(r'^search/$', views.show_flats, name='search_flats_page'),
    url(r'^admin/', admin.site.urls),
]
