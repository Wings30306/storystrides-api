"""
URL configuration for storystrides_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import ApiOverview, all_profiles, profile_detail, all_projects, project_detail, project_drafts, all_badges

urlpatterns = [

    path('admin/', admin.site.urls),
    path('profiles/', all_profiles, name='all-profiles'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
    path('projects/', all_projects, name='all-projects'),
    path('projects/<int:pk>/', project_detail, name='project-detail'),
    path('projects/<int:pk>/drafts/', project_drafts, name='project-drafts'),
    path('badges/', all_badges, name='all-badges'),
    path('', ApiOverview, name='api-overview'),
]
