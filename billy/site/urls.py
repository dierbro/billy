from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^api/', include('billy.site.api.urls')),
    (r'^browse/', include('billy.site.browse.urls')),
    (r'^web/', include('billy.site.www.urls')),
)
