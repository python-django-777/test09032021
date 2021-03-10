from django.urls import path
from upload import views

urlpatterns = [
    path('upload/', views.image_upload_view),
    path('all/', views.image_download),]