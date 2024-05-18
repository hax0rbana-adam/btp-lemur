from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from LemurAptana.LemurApp.api import router
from LemurAptana.LemurApp import views
from . import generic_views
from .views.inmate import inmate_search_proxy, inmate_add_searched, inmate_search, inmate_doc_autocomplete
from .views.order import order_build, order_create, order_add_book_isbn, order_add_book_custom, order_remove_book, order_send_out, order_unset, order_set, order_reopen, order_current
from .views.export import data_export
from django.conf.urls import *
from django.urls import re_path

# Lemur-specific views
urlpatterns = [ #patterns(
#  views,  # TODO: this is the wrong type...? We probably want to fix it and add it back in here
  re_path(r'^$', inmate_search, name='index'),
  re_path(r'^inmate/search/$', inmate_search, name='inmate-search'),
  re_path(r'^inmate/search/(?P<pk>\d+)/$', inmate_search, name='inmate-detail'),
  re_path(r'^inmate/add/searched/$', inmate_add_searched, name='inmate-add-searched'),
  re_path(r'^inmate_search_proxy/(?P<pk>\d+)/$', inmate_search_proxy, name='inmate-search-proxy'),
  re_path(r'^inmate/doc_autocomplete/$', inmate_doc_autocomplete, name='inmate-search-autocomplete'),
  re_path(r'^order/build/$', order_build, name='order-build'),
  re_path(r'^order/create/(?P<inmate_pk>\d+)/$', order_create, name='order-create'),
  re_path(r'^order/addbook/ISBN/$', order_add_book_isbn, name='order-add-book-ISBN'),
  re_path(r'^order/addbook/custom/$', order_add_book_custom, name='order-add-book-custom'),
  re_path(r'^order/removebook/(?P<book_pk>\d+)/$', order_remove_book, name='order-book-remove'),
  re_path(r'^order/sendout/$', order_send_out, name='order-send-out'),
  re_path(r'^order/unset/$', order_unset, name='order-unset'),
  re_path(r'^order/set/(?P<order_pk>\d+)/$', order_set, name='order-set'),
  re_path(r'^order/reopen/(?P<order_pk>\d+)/$', order_reopen, name='order-reopen'),
  re_path(r'^order/current/$', order_current, name='order-current'),
  re_path(r'^data_export/$', data_export, name='data-export'),
  # Generic views
  #'',
  re_path(r'^inmate/add/$', generic_views.InmateCreate.as_view(), name="inmate-add"),
  re_path(r'^order/list/$', generic_views.OrderList.as_view(), name="order-oldlist"),
  re_path(r'^order/cleanup/$', generic_views.OrderCleanupList.as_view(), name='order-cleanup'),
  re_path(r'^order/detail/(?P<pk>\d+)/$', generic_views.OrderDetail.as_view(), name="order-detail"),
  re_path(r'^order/invoice/(?P<pk>\d+)/$', generic_views.OrderInvoice.as_view(), name="order-invoice"),
  # API views
  re_path(r'^api/', include(router.urls)),
  re_path(r'^schema/$', get_schema_view(title='BTP API')),
  re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  re_path(r'^docs/', include_docs_urls(title='My API service'))
]
