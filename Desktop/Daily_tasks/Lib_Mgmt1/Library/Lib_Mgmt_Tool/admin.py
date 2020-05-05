from django.contrib import admin
from django.contrib.auth.models import Group
from .models import books


admin.site.site_header = 'Library Book management Portal'

#admin.site.disable_action('recent actions')

class DontLog:
    def log_addition(self, *args):
        return

    # Do same for log_change and log_deletion

# @admin.register(Category)
# class CategoryAdmin(DontLog, admin.ModelAdmin):
#     pass

def available(modeladmin, request, queryset):
    queryset.update(available=True)
available.short_description = "available"

def not_available(modeladmin, request, queryset):
    queryset.update(available=False)
not_available.short_description = "Not available"


class booksdata(admin.ModelAdmin):
    list_display = ('ISBN','title','author','genre','available')
    actions = [available,not_available]

admin.site.register(books, booksdata)
admin.site.unregister(Group)