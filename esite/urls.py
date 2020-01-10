"""esite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls

from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie
from graphene_django.views import GraphQLView

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from wagtail.images.views.serve import ServeView

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView
    from django.views.generic.base import RedirectView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(
            r'^favicon\.ico$', RedirectView.as_view(
                url=settings.STATIC_URL + 'img/bread-favicon.ico'
                )
            )
    ]

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        url(r'^test404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^test500/$', TemplateView.as_view(template_name='500.html')),
    ]

urlpatterns += [
    url(r'', include(wagtail_urls)),
]

urlpatterns += [
    url(r'^api/graphql', jwt_cookie(GraphQLView.as_view())),
    url(r'^api/graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True, pretty=True))),
    url(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),
]

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
