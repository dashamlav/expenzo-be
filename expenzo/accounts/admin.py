from django.contrib import admin
from .models import AppUser, AuthToken

admin.site.register([AppUser, AuthToken])

