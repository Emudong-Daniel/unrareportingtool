from django.contrib import admin
from .models import Complaint, StatusUpdate

admin.site.register(Complaint)
admin.site.register(StatusUpdate)
