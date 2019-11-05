
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'phone_number', 'biography', 'website', 'picture')
    list_display_links = ('user', 'website')
    list_editable = ('phone_number', 'biography')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            ),
        })
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)