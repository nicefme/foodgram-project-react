from django.contrib import admin

from users.models import CustomUser, Follow


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
       'id', 'username', 'email', 'first_name', 'last_name',
    )
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = (
       'id', 'user', 'author',
    )
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)
