from rest_framework import serializers
from ne_sop_api.utils import Utils
from django.conf import settings
from django.contrib.auth.models import User

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
    Group,
    User,
)


# %% GROUP
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


# %% USER
class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

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


# %% CURRENT USER
class CurrentUserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    groups = serializers.StringRelatedField(many=True)
    is_manager = serializers.SerializerMethodField("get_is_manager")

    def get_is_manager(self, obj):
        return obj.groups.filter(name="Manager").exists()

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "is_manager",
            "groups",
        ]


# %% EVENT TYPE
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


# %% ENTITY TYPE
class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ("id", "name", "service")


# %% ENTITY LIST
class EntityListSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Entity
        fields = [
            "id",
            "uuid",
            "name",
            "abbreviation",
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
            "valid",
        ]


# %% ENTITY
class EntitySerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=EntityType.objects.all())

    class Meta:
        model = Entity
        fields = [
            "id",
            "uuid",
            "name",
            "abbreviation",
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
            "users",
            "active",
            "valid",
        ]


# %% ITEM TYPE
class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = "__all__"


# %% ITEM STATUS
class ItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStatus
        fields = "__all__"


# %% ITEM LIST
class ItemListSerializer(serializers.ModelSerializer):
    type = ItemTypeSerializer(read_only=True)
    status = ItemStatusSerializer(read_only=True)
    author = serializers.StringRelatedField()
    lead = serializers.StringRelatedField()

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
            "late",
            # "islate",
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
            "startdate",
            "enddate",
            "valid",
        ]


# %% ITEM
class ItemSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=ItemType.objects.all(),
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset=ItemStatus.objects.all(),
    )

    author = serializers.PrimaryKeyRelatedField(
        queryset=Entity.objects.all(),
    )

    lead = serializers.PrimaryKeyRelatedField(
        queryset=Entity.objects.all(),
    )

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
            "late",
            # "islate",
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
            "autonotify",
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

    # %% ITEM STATISTICS


class ItemTypeStatisticsSerializer(serializers.ModelSerializer):
    num_items = serializers.IntegerField()
    year = serializers.DateField()

    class Meta:
        model = ItemType
        fields = [
            "name",
            "num_items",
            "year",
        ]


# %% EVENT LIST
class EventListSerializer(serializers.ModelSerializer):
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


# %% EVENT
class EventSerializer(serializers.ModelSerializer):
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


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


# %% TESTING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


class NewEventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=False)

    uuid = serializers.UUIDField(required=False, read_only=False)

    type = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all(),
    )

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


class UserFullNameSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=False)

    template = serializers.SlugRelatedField(slug_field="name", read_only=True)
    template_id = serializers.PrimaryKeyRelatedField(source="template", queryset=Template.objects.all(), write_only=True)

    author = UserFullNameSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source="author", queryset=User.objects.all(), default=serializers.CurrentUserDefault(), write_only=True)

    version = serializers.IntegerField(required=False)

    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = Document
        fields = [
            "id",
            "uuid",
            "created",
            "filename",
            "template",
            "template_id",
            "note",
            "version",
            "size",
            "item",
            "author",
            "author_id",
            "file",
        ]

    def create(self, validated_data):
        version = Utils.get_next_documentVersion(Document, validated_data)
        validated_data["version"] = version

        template = validated_data.get("template")

        file = validated_data.get("file", None)

        filename = file.name
        file_extension = filename.rsplit(".", 1)[1]

        if int(template.id) != int(settings.NESOP_TEMPLATE_AUTRE_ID):
            template = Template.objects.filter(id=template.id).first()
            filename = template.filename

        filename = filename.rsplit(".", 1)[0] + f"_v{version}." + file_extension

        file.name = filename
        validated_data["file"] = file
        validated_data["filename"] = filename

        document = Document.objects.create(**validated_data)
        return document


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

    documents = DocumentSerializer(required=False, many=True)

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
            "late",
            # "islate",
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
            "autonotify",
            "documents",
            "users",
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

    def update(self, instance, validated_data):
        new_events = validated_data.pop("events")
        support = validated_data.pop("support", None)

        instance.number = validated_data.get("number", instance.number)
        instance.type = validated_data.get("type", instance.type)
        instance.title = validated_data.get("title", instance.title)
        instance.status = validated_data.get("status", instance.status)
        instance.description = validated_data.get("description", instance.description)
        instance.urgent = validated_data.get("urgent", instance.urgent)
        # instance.late = validated_data.get("late", instance.late)
        instance.writtenresponse = validated_data.get("writtenresponse", instance.writtenresponse)
        instance.oralresponse = validated_data.get("oralresponse", instance.oralresponse)
        instance.author = validated_data.get("author", instance.author)
        instance.lead = validated_data.get("lead", instance.lead)
        instance.support.set(support)
        instance.autonotify = validated_data.get("autonotify", instance.autonotify)
        instance.valid = validated_data.get("valid", instance.valid)

        # for key, value in validated_data.items():
        #    setattr(instance, key, value)

        instance.save()

        # get all events related to item
        old_events = Event.objects.filter(item=instance.id)

        # delete all events related to item (and then replace them)
        # old_events.delete()

        """
        old_events_list = list((instance.events).all())

        id_old_events = Event.objects.filter(item=instance.pk).values_list(
            "id", flat=True
        )
        print("## id_old_events ---------------------------------------------------")
        print(id_old_events)

        print("## id_new_events ---------------------------------------------------")
        print(id_new_events)
        """

        # for id in id_old_events:
        #    if id not in id_new_events:
        #        Event.objects.get(id=id, item=instance).delete()

        id_new_events = [event.get("id", None) for event in new_events]
        for event in old_events:
            if event.id not in id_new_events:
                event.delete()

        for new_event in new_events:
            event_id = new_event.get("id", None)

            # IF EVENT ALREADY EXISTS, UPDATE IT
            if event_id:
                event_instance = Event.objects.get(id=event_id, item=instance)
                event_instance.date = new_event.get("date", event_instance.date)
                event_instance.time = new_event.get("time", event_instance.time)
                event_instance.type = new_event.get("type", event_instance.type)
                event_instance.description = new_event.get("description", event_instance.description)
                event_instance.valid = new_event.get("valid", event_instance.valid)
                event_instance.save()

            # IF EVENT DOES NOT EXISTS, CREATE IT
            else:
                Event.objects.create(item=instance, **new_event)

        return instance
