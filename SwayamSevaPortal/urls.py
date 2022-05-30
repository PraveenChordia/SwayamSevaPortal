"""SwayamSevaPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from SwayamSeva.views import (
    registration_view,
    login_view,
    home_view,
    logout_view,
    schemes_view,
    apply_view,
    docs_view,
    return_view,
    activate_view,
    profile_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register', registration_view, name="register"),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('schemes', schemes_view, name='schemes'),
    path('apply/<scheme>', apply_view, name='apply'),
    path('submitdoc/<scheme>', docs_view, name='docs'),
    path('return/<context>', return_view, name='return'),
    path('profile', profile_view, name='profile'),
    url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate_view,
         name='activate'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change.html'),
         name='password_change'),

    path('email_sent/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/set_password.html'), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),


]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SwayamSevaPortal Admin Panel'
admin.site.site_title = 'SwayamSevaPortal Admin'
admin.site.index_title = 'SSA Admin'

