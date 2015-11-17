from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

# Create your views here.
class Home(TemplateView):
  template_name = "home.html"

class InvestmentCreateView(CreateView):
  model = Investment
  template_name = 'investment/investment_form.html'
  fields = ['company', 'market', 'option', 'price', 'volume', 'description']
  success_url = reverse_lazy('investment_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(InvestmentCreateView, self).form_valid(form)

class InvestmentListView(ListView):
  model = Investment
  template_name = "investment/investment_list.html"

class InvestmentDetailView(DetailView):
  model = Investment
  template_name = "investment/investment_detail.html"

  def get_context_data(self, **kwargs):
    context = super(InvestmentDetailView, self).get_context_data(**kwargs)
    investment = Investment.objects.get(id=self.kwargs['pk'])
    analysis = Analysis.objects.filter(investment=investment)
    context['analysis'] = analysis
    user_analysis = Analysis.objects.filter(investment=investment, user=self.request.user)
    context['user_analysis'] = user_analysis
    return context

class InvestmentUpdateView(UpdateView):
  model = Investment
  template_name = 'investment/investment_form.html'
  fields = ['company', 'market', 'option', 'price', 'volume', 'description']

  def get_object(self, *args, **kwargs):
    object = super(InvestmentUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class InvestmentDeleteView(DeleteView):
  model = Investment
  template_name = 'investment/investment_confirm_delete.html'
  success_url = reverse_lazy('investment_list')

  def get_object(self, *args, **kwargs):
    object = super(InvestmentDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class AnalysisCreateView(CreateView):
  model = Analysis
  template_name = 'analysis/analysis_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.investment.get_absolute_url()

  def form_valid(self, form):
    investment = Investment.objects.get(id=self.kwargs['pk'])
    if Analysis.objects.filter(investment=investment, user=self.request.user).exists():
      raise PermissionDenied()
    form.instance.user = self.request.user
    form.instance.investment = Investment.objects.get(id=self.kwargs['pk'])
    return super(AnalysisCreateView, self).form_valid(form)

class AnalysisUpdateView(UpdateView):
  model = Analysis
  pk_url_kwarg = 'analysis_pk'
  template_name = 'analysis/analysis_form.html'
  fields = ['text']

  def get_object(self, *args, **kwargs):
    object = super(AnalysisUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

  def get_success_url(self):
    return self.object.investment.get_absolute_url()

class AnalysisDeleteView(DeleteView):
  model = Analysis
  pk_url_kwarg = 'analysis_pk'
  template_name = 'analysis/analysis_confirm_delete.html'

  def get_success_url(self):
    return self.object.investment.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(AnalysisDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    investment = Investment.objects.get(pk=form.data["investment"])
    try:
      analysis = Analysis.objects.get(pk=form.data["analysis"])
      prev_votes = Vote.objects.filter(user=user, analysis=analysis)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
          Vote.objects.create(user=user, analysis=analysis)
      else:
          prev_votes[0].delete()
      return redirect (reverse('investment_detail', args=[form.data["investment"]]))
    except:
      prev_votes = Vote.objects.filter(user=user, investment=investment)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
        Vote.objects.create(user=user, investment=investment)
      else:
        prev_votes[0].delete()
    return redirect('investment_list')
