from .views import *
from django.urls import path, include
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet)

urlpatterns = [
    # path('', include(router.urls)),

    path('api/v1/womenlist/', WomenAPIViews.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
]