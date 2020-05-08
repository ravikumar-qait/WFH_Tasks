from django.contrib import admin
from django.contrib.auth.models import Group , User
from .models import books, authors,genre
from django.contrib.admin import AdminSite
from django.contrib import sites


admin.site.site_header = 'Library Book management Portal'
admin.site.site_title = "Library Portal"
admin.site.index_title = ""


def stockout(modeladmin, request, queryset):
    queryset.update(quantity = 0)
    queryset.update(available= False)
stockout.short_description = "Out of Stock"

def available(modeladmin, request, queryset):
    queryset.update(available=True)
available.short_description = "Available"

def not_available(modeladmin, request, queryset):
    queryset.update(available=False)
not_available.short_description = "Not available"




class booksdata(admin.ModelAdmin):
    list_display = ('ISBN','title','author','genre','available')
    actions = [available,not_available,stockout]


admin.site.register(books, booksdata)
admin.site.register(authors)
admin.site.register(genre)
admin.site.unregister(Group)
admin.site.unregister(User)

#admin.site.unregister(Site)


class MyAdmin(AdminSite):
    pass

myadmin = MyAdmin(name='myadmin')
myadmin.register(User)



