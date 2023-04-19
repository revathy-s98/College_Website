from django.contrib import admin

# Register your models here.
from collegewebsite.models import Course, Department, Member

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Member)
