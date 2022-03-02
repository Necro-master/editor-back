from . import views
from django.urls import path

urlpatterns = [
    path('new_session/', views.new_session),
    path('<int:code_id>/edit/', views.edit_code),
    path('<int:code_id>/read/', views.read_code),
]