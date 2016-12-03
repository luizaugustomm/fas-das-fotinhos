from django.conf.urls import include, url

import tops.views

urlpatterns = [
    url(r'^$', tops.views.index, name='index'),
    url(r'^auth$', tops.views.auth, name='auth'),
    url(r'^auth_done$', tops.views.auth_done, name='auth_done'),
    url(r'^logout$', tops.views.logout, name='logout'),
    url(r'^privacy$', tops.views.privacy, name='privacy'),
]
