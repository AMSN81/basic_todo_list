from django.contrib import admin
from .models import todo

class todoAdmin(admin.ModelAdmin):
    list_display = ["name","user","progress_percent"]

    class Meta:
        Model=todo

admin.site.register(todo, todoAdmin)