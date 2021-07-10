from apis.models import Api
from rest_framework import viewsets, permissions
from .serializers import ApiSerializer

# Api Viewset
class ApiViewset(viewsets.ModelViewSet):
  queryset = Api.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]

  serializer_class = ApiSerializer