from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from members.models import Profile
from projects.models import Project, Draft, DraftBadge
from badges.models import Badge, Category, BadgeCategory
from .serializers import ProfileSerializer, ProjectSerializer, DraftSerializer, DraftBadgeSerializer, BadgeSerializer, CategorySerializer, BadgeCategorySerializer


@api_view(['GET'])
def ApiOverview(req):
    api_description = {
        'API Description': 'This is the API for StoryStrides, a platform for writers to share their projects and drafts. Here, you can also earn badges for different stages you reach in each draft. Happy writing!',
    }

    return Response(api_description)

# Specific view functioons for each model would go here, similar to the ApiOverview function above.
@api_view(['GET'])
def all_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['GET'])
def all_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['GET'])
def project_drafts(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    drafts = Draft.objects.filter(project=project)
    serializer = DraftSerializer(drafts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_badges(request):
    badges = Badge.objects.all()
    serializer = BadgeSerializer(badges, many=True)
    return Response(serializer.data)