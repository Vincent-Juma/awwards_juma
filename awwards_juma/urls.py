"""awwards_juma URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,re_path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path('^register/',user_views.register,name="register"),
    re_path('^profile/',user_views.profile,name="profile"),
    re_path('',include('main.urls')),
    re_path('^login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    re_path('^logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    re_path('^api/projects/$', views.ProjectList.as_view(),name="all_projects_api"),
    re_path('^api/profiles/$',views.ProfileList.as_view(),name="all_profiles_api"),
    re_path('^ajax/rate/(?P<pk>\d+)',views.AjaxRating,name="ajaxrating")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# GeneratorExit
