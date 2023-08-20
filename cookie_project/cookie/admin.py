from django.contrib import admin
from cookie.models import Accounts, Pet, Walk, Breed

admin.site.register(Accounts)
admin.site.register(Pet)
admin.site.register(Walk)
admin.site.register(Breed)

# Register your models here.
