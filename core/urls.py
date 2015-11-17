from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^investment/create/$', InvestmentCreateView.as_view(), name='investment_create'),   
  url(r'investment/$', InvestmentListView.as_view(), name='investment_list'),
  url(r'^investment/(?P<pk>\d+)/$', InvestmentDetailView.as_view(), name='investment_detail'),
  url(r'^investment/update/(?P<pk>\d+)/$', InvestmentUpdateView.as_view(), name='investment_update'),                      
)