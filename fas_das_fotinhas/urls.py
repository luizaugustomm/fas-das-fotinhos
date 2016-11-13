from django.conf.urls import include, url

import tops.views

# Examples:
# url(r'^$', 'fas_das_fotinhas.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', tops.views.index, name='index'),
    url(r'^auth$', tops.views.auth, name='auth'),
]
