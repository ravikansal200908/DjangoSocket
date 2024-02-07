from django.urls import path
from .views import HomeView

app_name = "app1_basic_setup"

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
