from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserRecord)
admin.site.register(ServiceType) 
admin.site.register(Subadmins)
admin.site.register(ratings_reviews)
admin.site.register(problem)