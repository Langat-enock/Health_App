from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import HealthProgram, Client, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name', 'last_name']
    list_filter = ('enrollment', 'enrollment__enrollment_date')
    inlines = [EnrollmentInline]
