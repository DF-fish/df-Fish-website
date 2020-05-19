from django.contrib import admin
from .models import Article

## if registered, those objects can be created from the GUI admin page

admin.site.register(Article)
