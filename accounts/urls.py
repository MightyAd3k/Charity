from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]
