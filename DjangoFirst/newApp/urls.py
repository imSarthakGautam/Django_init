from django.urls import path
from . import views

# localhost:8000/newApp
# localhost:8000/newApp/about
urlpatterns = [
  
    path('', views.myNewApp, name='myApp'),
    #path('faq/', views.faq, name='faq'),
    
]
