from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Complaint, Response, Evidence
from .forms import ComplaintForm, ResponseForm, EvidenceForm

class HomeView(View):
    def get(self, request):
        return render(request, "coreapp/home.html")

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        complaints = Complaint.objects.filter(user=request.user)
        pending_count = complaints.filter(status='pending').count()
        investigating_count = complaints.filter(status='investigating').count()
        resolved_count = complaints.filter(status='resolved').count()
        closed_count = complaints.filter(status='closed').count()
        
        context = {
            'complaints': complaints[:5],  # Latest 5 complaints
            'pending_count': pending_count,
            'investigating_count': investigating_count,
            'resolved_count': resolved_count,
            'closed_count': closed_count,
            'total_count': complaints.count(),
        }
        return render(request, "coreapp/dashboard.html", context)

class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'coreapp/complaint_list.html'
    context_object_name = 'complaints'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Complaint.objects.filter(user=self.request.user)
        status_filter = self.request.GET.get('status')
        if status_filter and status_filter != 'all':
            queryset = queryset.filter(status=status_filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', 'all')
        return context

class ComplaintDetailView(LoginRequiredMixin, DetailView):
    model = Complaint
    template_name = 'coreapp/complaint_detail.html'
    context_object_name = 'complaint'
    
    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        context['evidence_form'] = EvidenceForm()
        return context

class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'coreapp/complaint_form.html'
    success_url = reverse_lazy('coreapp:complaint_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Complaint submitted successfully!')
        return super().form_valid(form)

class ComplaintUpdateView(LoginRequiredMixin, UpdateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'coreapp/complaint_form.html'
    
    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user, status='pending')
    
    def get_success_url(self):
        return reverse_lazy('coreapp:complaint_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Complaint updated successfully!')
        return super().form_valid(form)

class ResponseCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
        form = ResponseForm(request.POST)
        
        if form.is_valid():
            response = form.save(commit=False)
            response.complaint = complaint
            response.is_from_police = False
            response.save()
            messages.success(request, 'Your response has been submitted.')
        else:
            messages.error(request, 'There was an error with your submission.')
            
        return redirect('coreapp:complaint_detail', pk=pk)

class EvidenceCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
        form = EvidenceForm(request.POST, request.FILES)
        
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.complaint = complaint
            evidence.save()
            messages.success(request, 'Evidence uploaded successfully.')
        else:
            messages.error(request, 'There was an error uploading your evidence.')
            
        return redirect('coreapp:complaint_detail', pk=pk)
