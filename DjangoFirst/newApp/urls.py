from django.urls import path
from . import views

# localhost:8000/newApp
# localhost:8000/newApp/about
urlpatterns = [
  
    path('', views.myNewApp, name='newApp'),
    path('<int:my_id>/', views.userDetails, name='userDetails'),
    path('player/', views.player, name='player'),
    #path('faq/', views.faq, name='faq'),
    
]
