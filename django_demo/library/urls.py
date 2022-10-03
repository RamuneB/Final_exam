from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('uzrasai/', views.UzrasasListView.as_view(), name='uzrasai'),
    path('uzrasai/<int:pk>', views.UzrasasDetailView.as_view(), name='uzrasas'),
    path('kategorijos/', views.kategorijos, name='kategorijos'),
    path('kategorijos/<int:kategorija_id>', views.kategorija, name='kategorija'),
    path('search/', views.search, name='search'),
    path('filter/', views.filter, name='filter'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path('myuzrasai/', views.LoanedUzrasaiByUserListView.as_view(), name='myuzrasai'),
    path('myuzrasai/<int:pk>', views.UzrasasByUserDetailView.as_view(), name='my-uzrasas'),
    path('myuzrasai/new', views.UzrasasByUserCreateView.as_view(), name='my-uzrasas-new'),
    path('myuzrasai/<int:pk>/update', views.UzrasasByUserUpdateView.as_view(), name='my-uzrasas-update'),
    path('myuzrasai/<int:pk>/delete', views.UzrasasByUserDeleteView.as_view(), name='my-uzrasas-delete'),
    path('mykategorijos/', views.LoanedKategorijosiByUserListView.as_view(), name='mykategorijos'),
    path('mykategorijos/<int:pk>', views.KategorijaByUserDetailView.as_view(), name='my-kategorija'),
    path('mykategorijos/new', views.KategorijaByUserCreateView.as_view(), name='my-kategorija-new'),
    path('mykategorijos/<int:pk>/update', views.KategorijaByUserUpdateView.as_view(), name='my-kategorija-update'),
    path('mykategorijos/<int:pk>/delete', views.KategorijaByUserDeleteView.as_view(), name='my-kategorija-delete'),
]
