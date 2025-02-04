from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.services.email_service import EmailService

from apps.user.models import ProfileModel

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            'id',
            'name',
            'surname',
            'age',
            'birthday',
            'phone',
            'country',
            'city',
            'nationality'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at',
            'last_login',
            'profile'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user

    @atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        profile_instance = instance.profile

        if profile_data:
            for attr, value in profile_data.items():
                setattr(profile_instance, attr, value)
            profile_instance.save()

        return instance

