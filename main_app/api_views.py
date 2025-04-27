# main_app/api_views.py

from rest_framework.generics import RetrieveAPIView
from .models import ClientProfile
from .serializers import ClientProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ClientProfileAPI(RetrieveAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]



