from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('src.dinner.views',
     (r'^cafeteria/(?P<cafeteria>\w+)/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', 'get_dinner'),
     # Example usage: api/cafeteria/Realfag/2011-3-7/
)
