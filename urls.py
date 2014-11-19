from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'forecast.views.index', name='index'),
)
