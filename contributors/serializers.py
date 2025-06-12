from rest_framework import serializers
from contributors.models import Contributor


class ContributorResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    project_id = serializers.IntegerField(source='project.id', read_only=True)

    class Meta:
        model = Contributor
        fields = ['user_id', 'project_id']
