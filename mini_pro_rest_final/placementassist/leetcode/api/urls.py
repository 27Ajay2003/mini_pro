# from django.urls import path,include
# from leetcode.api.views import ResultListAV,ResultDetailAV,ProfileListAV,ProfileDetailAV

# urlpatterns = [
#     path('result/',ResultListAV.as_view(),name='result-list'),
#     path('result/<int:pk>',ResultDetailAV.as_view(),name='result-details' ),
#     path('profile/',ProfileListAV.as_view(),name='profile-list'),
#     path('profile/<int:pk>',ProfileDetailAV.as_view(),name='profile-details')
    
# ]

from django.urls import path, include
from rest_framework import routers
from leetcode.api.views import ResultsViewSet
from leetcode.api.views import RegisterView,LoginView,UserView,LogoutView,ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'results', ResultsViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]