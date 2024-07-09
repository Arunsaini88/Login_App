from django.urls import path
from .views import signup, login_view,logout_view ,patient_dashboard, dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('dashboard/',dashboard, name='dashboard'),
]
