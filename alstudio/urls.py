from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'alstudio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^portfolio$', 'portfolio.views.portfolio_base'),
    url(r'^about$', 'about.views.about'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
