from rest_framework import serializers
from ne_sop_api.models import (
    Document,
    Entity,
    EntityType,
    Event,
    EventType,
    Item,
    ItemType,
    ItemStatus,
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


class ItemListSerializer(serializers.ModelSerializer):
    type = ItemTypeSerializer(read_only=True)
    status = ItemStatusSerializer(read_only=True)
    author = serializers.StringRelatedField()
    lead = serializers.StringRelatedField()

    # support = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = [
            "id",
            "uuid",
            "number",
            "title",
            "type",
            "status",
            "urgent",
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
            "valid",
        ]


class ItemSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=ItemType.objects.all(),
    )

    """" 
    type = ItemTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=ItemType.objects.all(),
        write_only=True,
    )
    """

    status = serializers.PrimaryKeyRelatedField(
        queryset=ItemStatus.objects.all(),
    )

    """
    status = ItemStatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        source="status",
        queryset=ItemStatus.objects.all(),
        write_only=True,
    )
    """

    author = serializers.PrimaryKeyRelatedField(
        queryset=Entity.objects.all(),
    )
    """
    author = EntitySerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=Entity.objects.all(),
        write_only=True,
    )
    """

    lead = serializers.PrimaryKeyRelatedField(
        queryset=Entity.objects.all(),
    )
    """
    lead = EntitySerializer(read_only=True)
    """

    """
    support = EntitySerializer(many=True, read_only=True)
    """

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

    """
    events = NestedEventerializer(many=True, read_only=True)
    """

    class Meta:
        model = Item
        fields = [
            "id",
            "uuid",
            "number",
            "title",
            "type",
            # "type_id",
            "status",
            "description",
            # "status_id",
            "urgent",
            "writtenresponse",
            "oralresponse",
            "author",
            # "author_id",
            "lead",
            "support",
            "events",
            "valid",
        ]


class NestedItemSerializer(serializers.ModelSerializer):
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


class EventListSerializer(serializers.ModelSerializer):
    # type = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())
    # type = serializers.StringRelatedField()
    type = EventTypeSerializer(read_only=True)
    item = NestedItemSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "uuid",
            "date",
            "time",
            "type",
            "item",
            "description",
            "valid",
        ]


class EventSerializer(serializers.ModelSerializer):
    """
    type = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all(),
    )
    """

    """
    type = EventTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        source="type",
        queryset=EventType.objects.all(),
        write_only=True,
    )
    """
    # item = NestedItemSerializer(read_only=True)
    # item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
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
            "item",
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


class DocumentByItemSerializer(serializers.ModelSerializer):
    template = serializers.SlugRelatedField(
        queryset=Template.objects.all(),
        slug_field='name',
    )
    class Meta:
        model = Document
        fields = [
            "created",
            "uuid",
            "template",
            "note",
            "valid",
            "relpath",
            "version",
            "filename",
        ]

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()



# %% TESTING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


class NewEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "uuid",
            "date",
            "time",
            "type",
            "description",
            "valid",
        ]


class NewItemSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=ItemType.objects.all(),
    )

    status = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=ItemStatus.objects.all(),
    )

    author = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Entity.objects.all(),
    )

    lead = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Entity.objects.all(),
    )

    support = serializers.PrimaryKeyRelatedField(
        required=False,
        many=True,
        queryset=Entity.objects.all(),
    )

    events = NewEventSerializer(required=False, many=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "uuid",
            "number",
            "title",
            "type",
            "status",
            "description",
            "urgent",
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
            "valid",
        ]

    def create(self, validated_data):
        events = validated_data.pop("events", None)
        support = validated_data.pop("support", None)
        item = Item.objects.create(**validated_data)

        item.support.set(support)

        if events is not None:
            for event in events:
                Event.objects.create(item=item, **event)

        return item
