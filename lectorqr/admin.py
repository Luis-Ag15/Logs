from django.contrib import admin
from .models import Alumno, ScanLog

admin.site.register(Alumno)

@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    list_display = ('scanner', 'alumno', 'timestamp')
    list_filter = ('timestamp', 'scanner')
    search_fields = ('scanner__username', 'alumno__id', 'alumno__nombre')
