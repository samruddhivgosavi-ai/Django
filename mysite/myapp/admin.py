from django.contrib import admin
from.models import Students
from.models import Employee
from.models import document
# Register your models here.
admin.site.register([Students])
admin.site.register([Employee])
admin.site.register([document])