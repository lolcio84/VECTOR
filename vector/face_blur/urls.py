from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello, name="hello_page"), 
    path("inter", views.inter), 
    path("", views.hub), 
    path("upload", views.upload_photo, name="upload"),
    path('show/', views.show_photos, name='show_photos'),
]