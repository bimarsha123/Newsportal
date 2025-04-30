from django.urls import re_path
from .import views

urlpatterns = [

    re_path(r'^$', views.home, name='home'),                        ## Front Home Page
    re_path(r'^about/$', views.about, name='about'),                ## Front About Page
    re_path(r'^category/$', views.category, name='category'),                ## Front About Page
    re_path(r'^panel/$', views.panel, name='panel'),                ## Admin Panel Home Page
    re_path(r'^login/$', views.mylogin, name='mylogin'),            ## Front Login Page
    re_path(r'^register/$', views.myregister, name='myregister'),    ## Front Register Page
    re_path(r'^logout/$', views.mylogout, name='mylogout'),         ## Front Logoout Page
    re_path(r'^panel/setting/$', views.site_setting, name='site_setting'),  ## Admin Panel Settings
    re_path(r'^panel/about/setting/$', views.about_setting, name='about_setting'),  ## This is for about(about seeting) in admin panel
    re_path(r'^contact/$', views.contact, name='contact'),          ## Front Contact Pages
    re_path(r'^panel/change/pass/$', views.change_pass, name='change_pass'),  ## Password Change (By clicking setting button in admin pannel)
]