from rest_framework import serializers
from .models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']

class ContributorResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    project_id = serializers.IntegerField(source='project.id')

    class Meta:
        model = Contributor
        fields = ['user_id', 'project_id']