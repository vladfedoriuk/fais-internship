from rest_framework import serializers
from core.models import Configuration, Release
from django.db.models import Model

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['name']


def get_serializer(model: Model) -> serializers.ModelSerializer:
    
    Meta = type('Meta', (object, ),{
        'model': model,
        'fields': ['parameters', 'valid_from', 'valid_to', 'version',]
    })
        
    class ConfigurationSerializer(serializers.ModelSerializer):
        
        @classmethod
        def model_name(cls):
            return cls.Meta.model.__name__
    
    ConfigurationSerializer.release = ReleaseSerializer()
    ConfigurationSerializer.Meta = Meta
        
    return ConfigurationSerializer

