from django.urls import path
from .views import main_index,category,course,payment,create_card,courses_page
app_name = 'main'

urlpatterns = [
    path('',main_index,name='index'),
    path('category/',category,name='category'),
    path('course/<int:pk>/',course,name='course'),
    path('payment/<int:pk>/',payment,name='payment'),
    path('card/<int:pk>/',create_card,name='card'),
    path('courses/<int:pk>/',courses_page,name='courses')
    
]