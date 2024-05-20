from rest_framework import routers
from kritikApp import views as kritikApps_views

router = routers.DefaultRouter()
router.register(r'establishment', kritikApps_views.EstablishmentViewSet)
router.register(r'review', kritikApps_views.ReviewViewSet)