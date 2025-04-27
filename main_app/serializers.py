
from rest_framework import serializers
from .models import ClientProfile, ProgramEnrollment

class ProgramEnrollmentSerializer(serializers.ModelSerializer):
    program = serializers.StringRelatedField()

    class Meta:
        model = ProgramEnrollment
        fields = ['program', 'enrollment_date']

class ClientProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    enrollments = ProgramEnrollmentSerializer(source='programenrollment_set', many=True)

    class Meta:
        model = ClientProfile
        fields = ['user', 'contact', 'medical_history', 'enrollments']
