from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    # Authentication
    path('accounts/login/', views.RoleLoginView.as_view(), name='login'),
    path('accounts/logout/', views.RoleLogoutView.as_view(), name='logout'),

    # 1. Complaint submission form
    path('', views.complaint_create, name='create'),

    # 2. Submission success page showing the new Complaint ID
    path('submitted/<int:pk>/', views.complaint_submitted, name='complaint_submitted'),

    # 3. Citizen status lookup
    path('lookup/', views.status_lookup, name='status_lookup'),

    # 4. Metrics dashboard (manager)
    path('dashboard/', views.dashboard, name='dashboard'),

    # 5. Admin assignment dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # 6. Technician dashboard
    path('technician-dashboard/', views.technician_dashboard, name='technician_dashboard'),

    # 7. Technician/manager status update
    path('complaint/<int:pk>/update/', views.complaint_update, name='complaint_update'),

    # 8. Reports (filter & export)
    path('reports/', views.reports, name='reports'),
]
