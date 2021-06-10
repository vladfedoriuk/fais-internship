from core.models import Files
from rest_framework import serializers


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        exclude = ["remarks", "file_name"]
