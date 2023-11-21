from django.contrib import admin

from .models import (
    Item,
    ItemType,
    ItemStatus,
    Entity,
    EntityType,
    Event,
    EventType,
    Template,
)

# Register your models here.
admin.site.register(Entity)
admin.site.register(EntityType)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(ItemStatus)
admin.site.register(Event)
admin.site.register(EventType)


# Widgets
class TemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ("parents",)


admin.site.register(Template, TemplateAdmin)
