from django.urls import path
from . import views

urlpatterns = [
   path("blur", views.blur, name="blur"), 
   path("", views.hub, name="hub")
]