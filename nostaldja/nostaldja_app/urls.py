from django.urls import path
from .import views


urlpatterns = [
    # path('', helloIndex),
    path('decades/', views.decades_list, name='decades_list'),
    path('decades/<int:id>', views.decades_show, name='decades_show'),

]
