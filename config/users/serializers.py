from rest_framework import serializers
from .models import User
import re

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'phone',
            'address',
            'state',
            'city',
            'country',
            'pincode',
            'profile_image'
        ]

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")
        if not re.search(r"\d", value):
            raise serializers.ValidationError("Password must contain at least one number")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # hashes password
        user.save()
        return user
