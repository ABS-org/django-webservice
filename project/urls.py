# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from rest_framework import routers
from project.apps.uploader.models import PhotoViewSet
from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),

		(r'^facebook/', include('django_facebook.urls')),
    
		(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    (r'^uploader/', include('project.apps.uploader.urls')),
	# (r'^$', RedirectView.as_view(url='/uploader/list/')), # Just for ease of use.

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
