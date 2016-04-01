from django.conf.urls import patterns, include, url

urlpatterns = patterns('services.views',    
    url(r'^$', 'servicelist', name='servicelist'),
    url(r'^service/(?P<pk>[0-9]+)/$', 'service_detail_home', name='service_detail_home'),
    url(r'^offer/$', 'offer', name='offer'),
    url(r'^(?P<pk>[0-9]+)/edit/$', 'edit_service', name='edit_service'),
    url(r'^(?P<pk>[0-9]+)/public/$', 'public_service', name='public_service'),
    url(r'^offer/(?P<pk>[0-9]+)/$', 'offer_detail_service', name='offer_detail_service'),
    url(r'^history/$', 'service_history', name='service_history')
)  
