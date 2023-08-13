from django.urls import path
from .views import index, top_sellers, advertisements_post, login, profile, register
from .models import Advertisements


urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisements_post, name='advertisement-post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
#    path('advertisements/', Advertisements, name='advertisements' )
]