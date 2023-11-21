from rest_framework import serializers
from ne_sop_api.models import (
    Entity,
    EntityType,
    Item,
    ItemType,
    ItemStatus,
    Event,
    EventType,
    Template,
    User,
)


# %% USER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "last_login",
            "username",
            "email",
            "is_active",
            "first_name",
            "last_name",
        ]


# %% ENTITY
class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    type = EntityTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EntityType.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Entity
        fields = [
            "id",
            "uuid",
            "name",
            "type",
            "type_id",
            "description",
            "street",
            "city",
            "postalcode",
            "region",
            "country",
            "region",
            "website",
            "email",
            "telephone",
            "valid",
        ]


# %% ITEM
class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = "__all__"


class ItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStatus
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    type = ItemTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=ItemType.objects.all(),
        write_only=True,
    )
    status = ItemStatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        source="status",
        queryset=ItemStatus.objects.all(),
        write_only=True,
    )
    author = EntitySerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=Entity.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "uuid",
            "number",
            "title",
            "type",
            "type_id",
            "status",
            "status_id",
            "author",
            "author_id",
            "valid",
        ]


# %% EVENT
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    type = EventTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EventType.objects.all(),
        write_only=True,
    )
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        source="item",
        queryset=Item.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "uuid",
            "date",
            "time",
            "type",
            "type_id",
            "item",
            "item_id",
            "description",
            "valid",
        ]


# %% TEMPLATE
class TemplateSerializer(serializers.ModelSerializer):
    parents = ItemTypeSerializer()

    class Meta:
        model = Template
        fields = [
            "id",
            "name",
            "parents",
            "valid",
        ]
