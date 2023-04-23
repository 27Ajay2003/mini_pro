from django.urls import path, include
from rest_framework import routers
from technicalquestions_api.api.views import ResultsViewSet,QuizQuestionViewSet

router = routers.DefaultRouter()
router.register(r'results', ResultsViewSet)
router.register(r'questions', QuizQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]