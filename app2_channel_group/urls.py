from django.urls import path
from .views import IndexView

app_name = "app2_channel_group"

urlpatterns = [
    path('index/', IndexView.as_view(), name='index')
]
