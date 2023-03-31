from django.contrib import admin

from base1.models import Database1


class admindatabase(admin.ModelAdmin):
    list_display = ["id","login","date","name","phone"]
    list_display_links = ["login"]

admin.site.register(Database1, admindatabase)