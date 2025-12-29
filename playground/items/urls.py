from rest_framework.routers import DefaultRouter

from playground.items import views

router = DefaultRouter()

router.register(r"items", views.ItemViewSet, basename="item")
router.register(r"items2", views.ItemViewSet, basename="item2")
