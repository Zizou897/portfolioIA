from django.contrib import admin
from .models import Service, Project, ContactMessage, Article

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin configuration for the Service model."""
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for the Project model."""
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'technologies_used')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'link')
        }),
        ('Categorization', {
            'fields': ('category', 'technologies_used')
        }),
        ('Date Information', {
            'fields': ('created_at',)
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin configuration for the ContactMessage model."""
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def has_add_permission(self, request):
        # Prevent adding contact messages from the admin
        return False

    def has_change_permission(self, request, obj=None):
        # Prevent changing contact messages from the admin
        return False

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin configuration for the Article model."""
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'image', 'content')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )
