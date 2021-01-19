from django.contrib import admin
from .models import User, Project, ProjectHrs

admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectHrs)

# Register your models here.
