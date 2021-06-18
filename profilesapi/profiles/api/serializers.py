from rest_framework import serializers
from profiles.models import Profile, ProfileStatus

class ProfileSerialzer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("avatar",)

class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    
    class Meta:
        model = ProfileStatus
        fields = "__all__"

