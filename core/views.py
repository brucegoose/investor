from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import *

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
    answers = Answer.objects.filter(investment=investment)
    context['analysis'] = answers
    return context

class InvestmentUpdateView(UpdateView):
  model = Investment
  template_name = 'investment/investment_form.html'
  fields = ['company', 'market', 'option', 'price', 'volume', 'description']

class InvestmentDeleteView(DeleteView):
  model = Investment
  template_name = 'investment/investment_confirm_delete.html'
  success_url = reverse_lazy('investment_list')

class AnswerCreateView(CreateView):
  model = Answer
  template_name = "answer/answer_form.html"
  fields = ['text']

  def get_success_url(self):
    return self.object.investment.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.investment = Investment.objects.get(id=self.kwargs['pk'])
    return super(AnswerCreateView, self).form_valid(form)
