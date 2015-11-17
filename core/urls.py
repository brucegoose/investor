from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^investment/create/$', login_required(InvestmentCreateView.as_view()), name='investment_create'),
  url(r'investment/$', login_required(InvestmentListView.as_view()), name='investment_list'),
  url(r'^investment/(?P<pk>\d+)/$', login_required(InvestmentDetailView.as_view()), name='investment_detail'),
  url(r'^investment/update/(?P<pk>\d+)/$', login_required(InvestmentUpdateView.as_view()), name='investment_update'),               url(r'^investment/delete/(?P<pk>\d+)/$', login_required(InvestmentDeleteView.as_view()), name='investment_delete'),
  url(r'^investment/(?P<pk>\d+)/analysis/create/$', login_required(AnalysisCreateView.as_view()), name='analysis_create'),
  url(r'^investment/(?P<investment_pk>\d+)/analysis/update/(?P<analysis_pk>\d+)/$', login_required(AnalysisUpdateView.as_view()), name='analysis_update'),
  url(r'^investment/(?P<investment_pk>\d+)/analysis/delete/(?P<analysis_pk>\d+)/$', login_required(AnalysisDeleteView.as_view()), name='analysis_delete'),
)
