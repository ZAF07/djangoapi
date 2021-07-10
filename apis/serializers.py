from rest_framework import serializers
from rest_framework.utils import field_mapping
from apis.models import Api

class ApiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Api
    fields = '__all__'