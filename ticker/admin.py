from django.contrib import admin

from .models import TickerText


@admin.register(TickerText)
class TickerTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', )
    fields = ('text', 'created_at', )
    readonly_fields = ('created_at', )
    list_filter = ('created_at', )
    search_fields = ('created_at', )
    ordering = ('created_at', )
