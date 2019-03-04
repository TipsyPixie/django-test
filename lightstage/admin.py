# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'created',
        'modified',
        'username',
        'is_active',
        'is_deleted',
        'is_blocked',
        'is_admin',
    )
    list_filter = (
        'last_login',
        'created',
        'modified',
        'is_active',
        'is_deleted',
        'is_blocked',
        'is_admin',
    )
