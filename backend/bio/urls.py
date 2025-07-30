from django.urls import path
from bio.api.views import UserProfileView

urlpatterns = [
    path('<str:username>/', UserProfileView.as_view(), name='user-profile'),
]