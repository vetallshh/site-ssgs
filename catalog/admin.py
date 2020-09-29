from django.contrib import admin
from .models import ReestrActive
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class BookResource(resources.ModelResource):

    class Meta:
        model = ReestrActive
        fields = [field.name for field in model._meta.fields if field.name != 'id']
        exclude = ['id']
        import_id_fields = ['lessName'] 


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(ReestrActive, BookAdmin)