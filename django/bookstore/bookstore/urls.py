"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from my_bookstore import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<title>.+)/(?P<book_id>[0-9]+)', views.book_page, name='book'),
    url(r'^category/(?P<cat>.+)/', views.cat_page, name='book'),
    url(r'^author/(?P<author>.+)/(?P<author_id>[0-9]+)', views.author_page, name='author'),
    url(r'^admin/', admin.site.urls),
    url(r'^test_forms/', views.test_forms),
    url(r'^test_session/', views.test_session),
]

# user account related
urlpatterns += [
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^delete_comment.*', views.delete_comment, name='delete_comment'),
  url(r'^logout/$', views.logout_view, name='logout'),
  url(r'^login.*', views.login_view, name='login'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
