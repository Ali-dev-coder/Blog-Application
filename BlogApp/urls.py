
from django.urls import path

from .views import home,catogery,postdetails,register,all_post_related_to_catogery
urlpatterns = [
    
    path('',home,name = 'home'),
    path('catogery/',catogery, name = 'catogery'),
    #path('post/',post, name = 'post'),
    path('post-details/<slug:url>',postdetails, name = 'post-details'),
    path('register/',register.as_view(), name = 'register'),
    #path('login/',login, name = 'login'),
    path('allpostonecatogery/<slug:url>',all_post_related_to_catogery, name = 'allpostonecatogery'),
]