from django.urls import path 

from . import views

app_name="encryption_decryption"

urlpatterns = [
    path("",views.encryption, name="encrypt"),
    path("decrypt/", views.decryption, name="decrypt")
]