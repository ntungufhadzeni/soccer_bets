from django.contrib import admin
from .models import Match


class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "last_update_at")


admin.site.register(Match, MatchAdmin)
