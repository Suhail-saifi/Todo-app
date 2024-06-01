from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete_item/<int:edit>', views.deleteitems, name='deleteitems'),
    path('update_item/<int:edit>', views.edititems, name='edititems'),
    
]
