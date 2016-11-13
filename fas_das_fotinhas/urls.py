from django.conf.urls import include, url

import tops.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', tops.views.index, name='index'),
]
