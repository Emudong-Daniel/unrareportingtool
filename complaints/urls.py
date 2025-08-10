# complaints/urls.py
from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint_create, name='create'),
    path('submitted/<int:pk>/', views.complaint_submitted, name='complaint_submitted'),
    path('lookup/', views.status_lookup, name='status_lookup'),
    path('metrics/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('technician/', views.technician_dashboard, name='technician_dashboard'),
    path('update/<int:pk>/', views.complaint_update, name='complaint_update'),
    path('reports/', views.reports, name='reports'),
    path('login/', views.RoleLoginView.as_view(), name='login'),
    path('logout/', views.RoleLogoutView.as_view(), name='logout'),
]
