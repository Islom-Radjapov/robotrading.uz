from django.contrib import admin

from clents_db.models import Database


class admindatabase(admin.ModelAdmin):
    list_display = ["id", "login", "date", "name", "phone"]
    list_display_links = ["login"]

admin.site.register(Database, admindatabase)