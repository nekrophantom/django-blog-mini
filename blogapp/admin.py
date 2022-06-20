from django.contrib import admin
from .models.user.user import User
from .models.blog.blog import Blog
# Register your models here.

admin.site.register(User)
admin.site.register(Blog)