from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  UserListView


urlpatterns = [
    path('', UserListView.as_view(),
        name='user-create'),
]