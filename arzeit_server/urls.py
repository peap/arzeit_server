from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from categories.models import Category
from tags.models import Tag
from timers.models import Timer, Interval

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


class UserViewSet(viewsets.ModelViewSet):
    model = User
class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
class TagViewSet(viewsets.ModelViewSet):
    model = Tag
class TimerViewSet(viewsets.ModelViewSet):
    model = Timer
class IntervalViewSet(viewsets.ModelViewSet):
    model = Interval

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'timers', TimerViewSet)
router.register(r'intervals', IntervalViewSet)

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
