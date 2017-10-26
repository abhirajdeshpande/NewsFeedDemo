from django.contrib import admin

from NewsHub.models import WorldData, UserClass


class GHSGAdmin(admin.AdminSite):
    site_header = 'CLSG Simulations'
    index_title = 'Administration Panel'


admin.site = GHSGAdmin()

# Register your models here.
admin.site.register(
    WorldData
)


class UserClassAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'world', 'country', 'role')
    list_per_page = 25
    search_fields = ('username', 'world', 'country', 'role')
    list_filter = ('world', 'country', 'role')


admin.site.register(
    UserClass,
    UserClassAdmin
)
