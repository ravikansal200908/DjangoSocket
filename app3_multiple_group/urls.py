from django.urls import path
from .views import IndexView

app_name = "app2_channel_group"

urlpatterns = [
    path('<str:group_name>/', IndexView.as_view(), name='index')
]
