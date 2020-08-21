from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cards.views import flash_cardViewSet


router = DefaultRouter()
router.register('flashcards', flash_cardViewSet)

urlpatterns = [
    path('', include(router.urls))
]