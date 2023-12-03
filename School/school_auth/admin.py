from django.contrib import admin
from django.contrib import messages
from import_export.admin import ImportExportModelAdmin



from .models import(
    User
)


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school',
        'email',
        'username',
        'firstName',
        'lastName',
        'role',
        'is_active',
        'is_staff',
        'is_superuser'
        )
    list_filter = ('username', 'role',)
    search_fields = ("username", 'role','is_active')

    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

admin.site.register(User, UserAdmin)
