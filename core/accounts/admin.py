# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import (CustomUserCreationForm, 
                    CustomUserChangeForm,
                    CustomAdminCreationForm,
                    CustomAdminChangeForm,
                    OperatoreCreationForm,
                    OperatoreChangeForm,
                    ResponsabileCreationForm,
                    ResponsabileChangeForm,
                    AssistenzaCreationForm,
                    AssistenzaChangeForm, 
                    )

from .models import(User,
                    Admin,
                    Operatore,
                    Responsabile,
                    Assistenza, 
                    )

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username","is_active","role","first_name","last_name","last_login"]
    list_display_links = ['username']
    admin_order = 1
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_superuser","is_staff", "is_active", "groups", "user_permissions")}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","password1", "password2","first_name","last_name")
            }
        ),
    )
    
    
    
class OperatoreAdmin(UserAdmin):
    add_form = OperatoreCreationForm
    form = OperatoreChangeForm
    list_display = ["username","is_active","role","first_name","last_name","last_login"]
    list_display_links = ['username']
    admin_order = 2
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","password1", "password2","first_name","last_name")
            }
        ),
    )    
    

class ResponsabileAdmin(UserAdmin):
    add_form = ResponsabileCreationForm
    form = ResponsabileChangeForm
    list_display = ["username","is_active","role","first_name","last_name","last_login"]
    list_display_links = ['username']
    admin_order = 3
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","password1", "password2","first_name","last_name")
            }
        ),
    )
    

class AssistenzaAdmin(UserAdmin):
    add_form = AssistenzaCreationForm
    form = AssistenzaChangeForm
    list_display = ["username","is_active","role","first_name","last_name","last_login"]
    list_display_links = ['username']
    admin_order = 4
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","password1", "password2","first_name","last_name")
            }
        ),
    )    
        
   


admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin,OperatoreAdmin)
admin.site.register(Operatore,OperatoreAdmin)
admin.site.register(Responsabile,ResponsabileAdmin)
admin.site.register(Assistenza,AssistenzaAdmin)



