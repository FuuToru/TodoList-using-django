from django.contrib import admin
from .models import Todo,PersonalInfo, Education, Project

# Register your models here.

admin.site.register(Todo)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Project)