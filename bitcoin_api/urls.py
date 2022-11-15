from django.urls import path, include
from rest_framework import routers

from bitcoin_api.views import BitcoinViewSet, LoginView,LogoutView,RegisterView

router = routers.DefaultRouter()
router.register(r'bitcoin', BitcoinViewSet, basename='bitcoin')

urlpatterns = [
    path('', include(router.urls)),
    path('user/login/', LoginView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('user/register/', RegisterView.as_view()),
]
