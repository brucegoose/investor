from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^investment/create/$', InvestmentCreateView.as_view(), name='investment_create'),
  url(r'investment/$', InvestmentListView.as_view(), name='investment_list'),
  url(r'^investment/(?P<pk>\d+)/$', InvestmentDetailView.as_view(), name='investment_detail'),
  url(r'^investment/update/(?P<pk>\d+)/$', InvestmentUpdateView.as_view(), name='investment_update'),               url(r'^investment/delete/(?P<pk>\d+)/$', InvestmentDeleteView.as_view(), name='investment_delete'),
  url(r'^investment/(?P<pk>\d+)/analysis/create/$', AnalysisCreateView.as_view(), name='analysis_create'),
  url(r'^investment/(?P<investment_pk>\d+)/analysis/update/(?P<analysis_pk>\d+)/$', AnalysisUpdateView.as_view(), name='analysis_update'),
  url(r'^investment/(?P<investment_pk>\d+)/analysis/delete/(?P<analysis_pk>\d+)/$', AnalysisDeleteView.as_view(), name='analysis_delete'),
)
