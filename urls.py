from django.conf.urls.defaults import patterns, include, url
from app import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin #HP uncommented
admin.autodiscover() #HP uncommented

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    #HP Important general shit

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), #HP uncommented
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), #HP uncommented
    #HP this serves our media files the easy(ish) way. 
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), #HP
    url(r'', include('social_auth.urls')),

    #HP the real pages

    (r'^$', views.login, {}, "Home"),
    (r'^about/$', views.about, {}, "About"),
    (r'home/$', views.home, {}, "Search"),
    (r'^search/$', views.search, {}, "Results"),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^addrecipe/$', views.addrecipe, {}, "addrecipe"),
    #HP add pages 
)
