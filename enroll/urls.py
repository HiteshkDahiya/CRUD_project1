from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='deletedata'),
    path('update/<int:id>/',views.update,name='updatedata'),
]