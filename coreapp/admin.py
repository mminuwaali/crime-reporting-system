from django.contrib import admin
from .models import Complaint, Response, Evidence

class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0

class EvidenceInline(admin.TabularInline):
    model = Evidence
    extra = 0

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ResponseInline, EvidenceInline]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'is_from_police', 'created_at')
    list_filter = ('is_from_police', 'created_at')
    search_fields = ('message', 'complaint__title')

@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'description', 'uploaded_at')
    search_fields = ('description', 'complaint__title')
