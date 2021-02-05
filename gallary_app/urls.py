from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_upload_view),
    path('add_category', views.add_category),
    path('view_image', views.view_image),
]