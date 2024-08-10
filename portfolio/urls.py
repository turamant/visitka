from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact-requests/', views.contact_requests, name='contact_requests'),
    path('contact-requests/<int:pk>/delete/', views.delete_contact_request, name='delete_contact_request'),
]
