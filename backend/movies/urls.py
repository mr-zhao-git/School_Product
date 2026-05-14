from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeHighScoreView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('recommend/', views.RecommendationView.as_view()),
    path('hot/', views.HotRankingView.as_view()),
    path('ratings/', views.RatingView.as_view()),
    path('favorites/', views.FavoriteView.as_view()),
    path('export/', views.ExportRecommendationView.as_view()),
    path('dashboard/', views.DashboardStatsView.as_view()),
    path('users/', views.UserManageView.as_view()),
]
