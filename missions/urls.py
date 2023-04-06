from django.urls import path
from . import views
from .models import Sermon


urlpatterns = [
    path('', views.home, name='index'),
    path('testimony/', views.testimony, name='testimony'),
    path('donate/', views.donate, name='donate'),
    path('about/', views.about, name='about'),
    path('sermons/', views.sermon, name='sermon'),
    path('discipleship/', views.discipleship, name='discipleship'),
    path('media/', views.media, name='media'),
    path('contact/', views.contact, name='contact'),
    path('sermons/<int:id>/', views.download, name='download'),

]