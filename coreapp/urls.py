from . import views
from django.urls import path

app_name = "coreapp"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    
    # Complaint URLs
    path("complaints/", views.ComplaintListView.as_view(), name="complaint_list"),
    path("complaints/new/", views.ComplaintCreateView.as_view(), name="complaint_create"),
    path("complaints/<int:pk>/", views.ComplaintDetailView.as_view(), name="complaint_detail"),
    path("complaints/<int:pk>/edit/", views.ComplaintUpdateView.as_view(), name="complaint_update"),
    
    # Response and Evidence URLs
    path("complaints/<int:pk>/respond/", views.ResponseCreateView.as_view(), name="response_create"),
    path("complaints/<int:pk>/evidence/", views.EvidenceCreateView.as_view(), name="evidence_create"),
]
