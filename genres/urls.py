from django.urls import path # type: ignore
# from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from . import views

urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
