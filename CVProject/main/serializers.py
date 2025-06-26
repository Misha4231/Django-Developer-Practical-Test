from rest_framework.serializers import ModelSerializer

from .models import CV

class CVSerializer(ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'