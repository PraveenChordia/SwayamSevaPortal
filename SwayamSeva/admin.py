from django.contrib import admin
from SwayamSeva.models import UserDetails, Schemes, Documents, CompleteUserDetails, Profile
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'EMAIL', 'first_name',
                    'date_joined', 'last_login', 'is_staff', 'is_active')
    search_fields = ('username', 'EMAIL', 'first_name ')
    readonly_fields = ('date_joined', 'last_login',)
    list_filter = ('username', 'EMAIL', 'first_name', 'is_active', 'is_staff')

    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = ((None, {'fields': ('username', 'EMAIL', 'first_name',
                                    'last_name')}),
                 ('Permissions', {'fields': ('is_staff', 'is_active',
                                             'groups', 'user_permissions')}),
                 ('Personal', {'fields': ('about',)}),
                 ('Other', {'fields': ('date_joined', 'last_login')}),)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        disabled_fields = set()
        # s_fields = 'is_active'

        if not request.user.is_superuser or not request.user.is_admin:
            disabled_fields |= {
                'is_active',
                'is_staff',
                'groups',
                'user_permissions'
            }
            if (
                    (not request.user.is_superuser or not request.user.is_admin)
                    and obj is not None
                    and obj == request.user
            ):
                disabled_fields |= {
                    'is_staff',
                    'is_admin',
                    'groups',
                    'user_permissions'
                }

            for f in disabled_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True
        return form

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class MyProfile(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]
    search_fields = ('user',)


class MySchemes(admin.ModelAdmin):
    list_display = ('Aadhaar', 'Scheme_Name', 'Status', 'Date_Applied')
    search_fields = ('Scheme_Name', 'Aadhaar', 'Status')
    readonly_fields = ('Date_Applied',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MyDocuments(admin.ModelAdmin):
    list_display = [field.name for field in Documents._meta.get_fields()]
    search_fields = ('Did', 'Uid', 'Pan_no')
    readonly_fields = ('Did', 'Uid', 'Date_Submitted')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MyCompleteUserDetails(admin.ModelAdmin):
    list_display = ('UDid', 'Aadhaar', 'F_name', 'Date_Submitted')

    search_fields = ('UDid', 'Aadhaar', 'F_name')
    readonly_fields = ('UDid', 'Date_Submitted')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserDetails, MyUserAdmin)
admin.site.register(Profile, MyProfile)
admin.site.register(CompleteUserDetails, MyCompleteUserDetails)
admin.site.register(Documents, MyDocuments)
admin.site.register(Schemes, MySchemes)
