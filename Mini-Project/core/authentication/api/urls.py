from django.urls import path, include
from rest_framework import routers
from authentication.api.views import RegisterView, LoginView, UserView, ProfileViewSet,RefreshTokenView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('refresh/', RefreshTokenView.as_view()),  # send refresh token obtained from login as a post request to get new access token
    path('', include(router.urls)),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]