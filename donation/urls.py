from django.urls import path

from donation import views


urlpatterns = [
    path('add_donation/', views.AddDonation.as_view(), name='add_donation')
]
