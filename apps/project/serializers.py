from rest_framework import serializers
from apps.project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'start_date', 'end_date', 'budget', 'status']

        