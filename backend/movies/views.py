import csv
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q
from django.http import HttpResponse
from rest_framework import generics, views
from rest_framework.response import Response
from .models import Movie, Rating, Favorite
from .serializers import MovieSerializer, RatingSerializer, FavoriteSerializer


class HomeHighScoreView(generics.ListAPIView):
    queryset = Movie.objects.filter(status='online').order_by('-avg_score')[:20]
    serializer_class = MovieSerializer


class CategoryView(views.APIView):
    def get(self, request):
        category = request.query_params.get('category')
        qs = Movie.objects.filter(status='online')
        if category:
            qs = qs.filter(category=category)
        return Response(MovieSerializer(qs[:50], many=True).data)


class RecommendationView(views.APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        watched = Rating.objects.filter(user_id=user_id).values_list('movie_id', flat=True)
        pref_cats = Rating.objects.filter(user_id=user_id).values('movie__category').annotate(c=Count('id')).order_by('-c')
        cat = pref_cats[0]['movie__category'] if pref_cats else None
        qs = Movie.objects.filter(status='online').exclude(id__in=watched)
        if cat:
            qs = qs.filter(category=cat)
        qs = qs.order_by('-hot_index', '-avg_score')[:20]
        return Response(MovieSerializer(qs, many=True).data)


class HotRankingView(generics.ListAPIView):
    queryset = Movie.objects.filter(status='online').order_by('-hot_index', '-avg_score')[:20]
    serializer_class = MovieSerializer


class RatingView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Favorite.objects.filter(user_id=user_id)


class ExportRecommendationView(views.APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        rec = RecommendationView().get(request).data
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="user_{user_id}_recommendation.csv"'
        writer = csv.writer(response)
        writer.writerow(['电影名', '分类', '评分', '热度'])
        for m in rec:
            writer.writerow([m['title'], m['category'], m['avg_score'], m['hot_index']])
        return response


class DashboardStatsView(views.APIView):
    def get(self, request):
        watch = Rating.objects.values('user__username').annotate(total=Count('id')).order_by('-total')[:10]
        search = Movie.objects.values('category').annotate(total=Count('id')).order_by('-total')
        good = Rating.objects.filter(score__gte=4).count()
        bad = Rating.objects.filter(score__lte=2).count()
        return Response({'watch': list(watch), 'search': list(search), 'good': good, 'bad': bad})


class UserManageView(views.APIView):
    def get(self, request):
        users = list(User.objects.values('id', 'username', 'email', 'is_active'))
        return Response(users)
