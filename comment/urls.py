from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/comment', CommentViewSet)

urlpatterns = []

urlpatterns += router.urls
