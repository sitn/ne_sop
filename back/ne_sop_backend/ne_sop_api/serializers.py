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


# %% EVENT
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


class NestedEventerializer(serializers.ModelSerializer):
    type = EventTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EventType.objects.all(),
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
            "description",
            "valid",
        ]


# %% ENTITY
class EntityTypeSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source="name")

    class Meta:
        model = EntityType
        fields = ("id", "name")
        # fields = "__all__"


"""         fields = (
            [
                "name",
            ],
        ) """


class EntityListSerializer(serializers.ModelSerializer):
    """
    type = EntityTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EntityType.objects.all(),
        write_only=True,
    )
    """

    type = serializers.StringRelatedField()
    # type = EntityTypeSerializer(read_only=True)
    # type = serializers.PrimaryKeyRelatedField(queryset=EntityType.objects.all())

    class Meta:
        model = Entity
        fields = [
            "id",
            "uuid",
            "name",
            "type",
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
            "valid",  # "type_id",
        ]


class EntitySerializer(serializers.ModelSerializer):
    """
    type = EntityTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EntityType.objects.all(),
        write_only=True,
    )
    """

    type = serializers.PrimaryKeyRelatedField(queryset=EntityType.objects.all())

    class Meta:
        model = Entity
        fields = [
            "id",
            "uuid",
            "name",
            "type",
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
            "valid",  # "type_id",
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

    lead = EntitySerializer(read_only=True)
    support = EntitySerializer(many=True, read_only=True)
    """
    lead_id = serializers.PrimaryKeyRelatedField(
        source="lead",
        queryset=Entity.objects.all(),
        write_only=True,
    )
    """

    """
    events = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    """

    """
    events = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Event.objects.all(),
     )
     source="events",
    """

    events = NestedEventerializer(many=True, read_only=True)

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
            "urgent",
            "writtenresponse",
            "oralresponse",
            "author",
            "author_id",
            "lead",
            "support",
            "events",
            "valid",
        ]


# %% EVENT


class EventSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())

    """
    type = EventTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EventType.objects.all(),
        write_only=True,
    )
    """

    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    """
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        source="item",
        queryset=Item.objects.all(),
        write_only=True,
    )
    """

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
    item_types = ItemTypeSerializer()

    class Meta:
        model = Template
        fields = [
            "id",
            "name",
            "item_types",
            "valid",
        ]
