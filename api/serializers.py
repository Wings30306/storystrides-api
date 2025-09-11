from django.db.models import fields
from rest_framework import serializers
from members.models import Profile
from projects.models import Project, Draft, DraftBadge
from badges.models import Badge, Category, BadgeCategory


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'location')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = ('id', 'project', 'title', 'content', 'created_at', 'updated_at')

class DraftBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftBadge
        fields = ('id', 'draft', 'badge')
        extra_kwargs = {
            'draft': {'required': True},
            'badge': {'required': True}
        }

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'name', 'description', 'image', 'created_at', 'updated_at') 
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'image': {'required': False}
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False}
        }

class BadgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BadgeCategory
        fields = ('id', 'badge', 'category')
        extra_kwargs = {
            'badge': {'required': True},
            'category': {'required': True}
        }
