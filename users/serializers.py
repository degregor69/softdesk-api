from rest_framework import serializers
from users.models import User


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password", "birth_date", "can_be_contacted", "can_data_be_shared"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("Vous devez avoir au moins 15 ans.")
        return value
