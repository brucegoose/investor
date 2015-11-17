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

class InvestmentUpdateView(UpdateView):
  model = Investment
  template_name = 'investment/investment_form.html'
  fields = ['company', 'market', 'option', 'price', 'volume', 'description']
  
class InvestmentDeleteView(DeleteView):
  model = Investment
  template_name = 'investment/investment_confirm_delete.html'
  success_url = reverse_lazy('investment_list')
