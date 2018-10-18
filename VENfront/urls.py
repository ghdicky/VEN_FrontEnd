from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loggedin/$', views.loggedin),     #link the view for loggedin
    url(r'^loggedout/$', views.loggedout),   #link the view for logged out
    url(r'^invalid/$', views.invalid),       #link the view for invalid
    url(r'^gview/$', views.googleview),         #link the view for invalid
    url(r'^mysqlveninfo/$', views.ajax_get_ven_info), #link the view for calling ajax_get_ven_info in views.py
    url(r'^mysqldefaultoptmode/$', views.ajax_get_defaultoptmode), #link the view for calling ajax_get_defaultoptmode in views.py
    url(r'^mysqlvenlog/$', views.ajax_get_ven_log), #link the view for calling ajax_get_ven_log in views.py
    url(r'^mysqlvenevent/$', views.ajax_get_ven_event), #link the view for calling ajax_get_ven_event in views.py
    url(r'^mysqlveneventactiveperiod/$', views.ajax_get_ven_event_active_period), #link the view for calling ajax_get_ven_event_active_period in views.py
    url(r'^mysqlveneventsignal/$', views.ajax_get_ven_event_signal), #link the view for calling ajax_get_ven_event_signal in views.py
    # link the view for calling ajax_get_defaultoptmode in views.py

]