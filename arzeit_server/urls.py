from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

import categories.views
import tags.views
import timers.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


class UserViewSet(viewsets.ModelViewSet):
    model = User
class GroupViewSet(viewsets.ModelViewSet):
    model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'categories', categories.views.CategoryViewSet)
router.register(r'tags', tags.views.TagViewSet)
router.register(r'timers', timers.views.TimerViewSet)
router.register(r'intervals', timers.views.IntervalViewSet)

urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Examples:
    # url(r'^$', 'arzeit_server.views.home', name='home'),
    # url(r'^arzeit_server/', include('arzeit_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
