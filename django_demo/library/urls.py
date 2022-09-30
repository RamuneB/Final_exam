from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzrasai/', views.UzrasasListView.as_view(), name='uzrasai'),
    path('uzrasai/<int:pk>', views.UzrasasDetailView.as_view(), name='uzrasas'),
    path('kategorijos/', views.kategorijos, name='kategorijos'),
    path('kategorijos/<int:kategorija_id>', views.kategorija, name='kategorija'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
]
