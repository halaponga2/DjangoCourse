from email.policy import default
from django.urls import include, path
from main.views import *
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()
router.register('shop', ShopViewSet)
router.register ('goods', GoodsViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('api/', include(router.urls)),
    path('sentry-debug/', trigger_error),
]