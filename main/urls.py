from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^$',views.Index_view,name="index_view"),
    re_path(r'^upload/$',views.Upload_Project,name="upload_project"),
    re_path(r'^rating/(?P<pk>\d+)$',views.RateProject,name="rate_project"),
    re_path(r'^myprofile/',views.User_Profile,name="my_profile"),
    re_path(r'^devcenter/',views.Dev_center,name="dev_center")
]