from django.contrib import admin
from .models import Text, Author,Stats
# Register your models here.

admin.site.register(Text)
admin.site.register(Author)
admin.site.register(Stats)

