from django.urls import path
from .views import RegisterView, LoginView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/users/', UserListView.as_view(), name='user-list-api'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
