from django.contrib import admin
from .models import Journalist, News,ContactMessage

admin.site.register(Journalist)
admin.site.register(News)
admin.site.register(ContactMessage)
