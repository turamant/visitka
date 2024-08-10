from django.contrib import admin
from .models import Skill, Project, Service, ContactRequest

# Register your models here.

@admin.register(Skill)
class AdminSkill(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    
    
@admin.register(Service)    
class AdminService(admin.ModelAdmin):
    list_display = ('name', 'description')
    

@admin.register(ContactRequest)
class AdminContactRequest(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
