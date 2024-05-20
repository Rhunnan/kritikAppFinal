from rest_framework import viewsets
from . import models
from . import serializers


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = models.Establishment.objects.all()
    serializer_class = serializers.EstablishmentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer