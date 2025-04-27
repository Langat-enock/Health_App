# views.py

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import ClientRegistrationForm
from .models import ClientProfile, HealthProgram, ProgramEnrollment
from .serializers import ClientProfileSerializer


# Register a New Client
def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Make sure 'login' is the correct name in your urls.py
    else:
        form = ClientRegistrationForm()
    return render(request, 'register_client.html', {'form': form})

# Enroll a Client in Programs
@login_required
def enroll_in_program(request, program_id):
    program = get_object_or_404(HealthProgram, id=program_id)
    client_profile= get_object_or_404(ClientProfile, user=request.user)
    ProgramEnrollment.objects.get_or_create(client=client_profile, program=program)
    return redirect('client_profile')  # Again, check if 'client_profile' is correctly named in your urls.py

# Search for Clients
class ClientSearchView(ListView):
    model = ClientProfile
    template_name = 'client_search.html'
    context_object_name = 'clients'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return ClientProfile.objects.filter(
            Q(user__username__icontains=query) | Q(contact__icontains=query)
        )

# View Client Profile
@login_required
def client_profile(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    enrollments = ProgramEnrollment.objects.filter(client=client)
    return render(request, 'client_profile.html', {'client': client, 'enrollments': enrollments})



