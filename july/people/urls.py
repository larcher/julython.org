from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('july.people.views',
    url(r'^location/$', 'locations', name='locations'),
    url(r'^location/(?P<location_slug>[a-zA-Z0-9\-]+)/$', 'users_by_location', name='member-list'),
    url(r'^projects/$', 'projects', name='projects'),
    url(r'^projects/(?P<slug>.+)/$', 'project_details', name='project-details'),
    url(r'^(?P<username>[a-zA-Z0-9_]+)/$', 'user_profile', name='member-profile'),
    url(r'^(?P<username>[a-zA-Z0-9_]+)/edit/$', 'edit_profile', name='edit-profile'),
    url(r'^(?P<username>[a-zA-Z0-9_]+)/email/(?P<email>.*)$', 'delete_email', name='delete-email'),
    url(r'^(?P<username>[a-zA-Z0-9_]+)/projects/$', 'people_projects', name='user-projects'),
)
