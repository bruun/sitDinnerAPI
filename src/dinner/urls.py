from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('src.dinner.views',
    (r'^cafeterias/$', 'get_cafeterias'),
    (r'^cafeteria/(?P<cafeteria>\w+)/today/$', 'get_dinner_for_today'),
    (r'^cafeteria/(?P<cafeteria>\w+)/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', 'get_dinner_for_day'),

    (r'^cafeteria/(?P<cafeteria>\w+)/this_week/$', 'get_dinner_for_this_week'),
    (r'^cafeteria/(?P<cafeteria>\w+)/weekly/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', 'get_dinner_for_week_by_day'),     # Example usage: api/cafeteria/Realfag/2011-3-7/
)
