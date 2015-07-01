from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.views.static import serve
from content.views import *


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	# (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^site_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

	url( r'^$', index, name = 'index' ),
	url( r'^activities/$', activities, name = 'activities' ),
	url( r'^contact_us/$', contact_us, name = 'contact_us' ),
	url( r'^availability/$', availability, name = 'availability' ),
	url( r'^contact_message/$', contact_message, name = 'contact_message' ),
	url( r'^accommodation/(?P<accommodation_id>\d+)/$', accommodation, name = 'accommodation' ),
]
