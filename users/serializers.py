from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from users.validations import validate_username

user_model = get_user_model()

class UserRegsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'
    def create(self, clean_data):
        user_obj = user_model.objects.create_user(email=clean_data['email'],
                                                  username=clean_data['username'],
                                                  password=clean_data['password'])
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, cleaned_data):
        user = authenticate(email=cleaned_data['email'], password=cleaned_data['password'])
        if not user:
            raise serializers.ValidationError('User not found')
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: user_model
        fields = ('email', 'username')