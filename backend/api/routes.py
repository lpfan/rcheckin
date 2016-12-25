from rest_framework import routers

from .views import JournalViewSet


api_router = routers.SimpleRouter()
api_router.register('journal', JournalViewSet)
