from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'priority',
                  'tag', 'status', 'assigned_to']
