from django.urls import path
from . import views

app_name='flotta'

urlpatterns = [
    path('crea-categorie/', views.CategorieViewCreate.as_view(), name='categorie_create'),
    path('lista-categorie/', views.CategorieViewList.as_view(), name='categorie_list'),
    path('update-categorie/<int:pk>/', views.CategorieViewUpdate.as_view(), name='categorie_update'),
    path('detail-categorie/<int:pk>/', views.CategorieViewDetail.as_view(), name='categorie_detail'),
    path('delete-categorie/<int:pk>/', views.CategorieViewDelete.as_view(), name='categorie_delete'),
]

urlpatterns += [
    path('crea-mezzi/', views.MezziViewCreate.as_view(), name='mezzi_create'),
    path('lista-mezzo/', views.MezziViewList.as_view(), name='mezzi_list'),
    path('update-mezzi/<int:pk>/', views.MezziViewUpdate.as_view(), name='mezzi_update'),
    path('detail-mezzi/<int:pk>/', views.MezziViewDetail.as_view(), name='mezzi_detail'),
    path('delete-ute/<int:pk>/', views.MezziViewDelete.as_view(), name='mezzi_delete'),
]

