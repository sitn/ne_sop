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


# %% EVENT TYPE
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


# %% ENTITY TYPE
class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ("id", "name")


# %% ENTITY LIST
class EntityListSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

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
            "writtenresponse",
            "oralresponse",
            "author",
            "lead",
            "support",
            "events",
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
            "writtenresponse",
            "oralresponse",
            "author",
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
    parents = ItemTypeSerializer()

    class Meta:
        model = Template
        fields = [
            "id",
            "name",
            "parents",
            "valid",
        ]


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

    def update(self, instance, validated_data):
        new_events = validated_data.pop("events")
        support = validated_data.pop("support", None)

        instance.number = validated_data.get("number", instance.number)
        instance.type = validated_data.get("type", instance.type)
        instance.title = validated_data.get("title", instance.title)
        instance.status = validated_data.get("status", instance.status)
        instance.description = validated_data.get("description", instance.description)
        instance.urgent = validated_data.get("urgent", instance.urgent)
        instance.writtenresponse = validated_data.get(
            "writtenresponse", instance.writtenresponse
        )
        instance.oralresponse = validated_data.get(
            "oralresponse", instance.oralresponse
        )
        instance.author = validated_data.get("author", instance.author)
        instance.lead = validated_data.get("lead", instance.lead)
        instance.support.set(support)
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
                print("Update (event exists)")
                event_instance = Event.objects.get(id=event_id, item=instance)
                event_instance.date = new_event.get("date", event_instance.date)
                event_instance.time = new_event.get("time", event_instance.time)
                event_instance.type = new_event.get("type", event_instance.type)
                event_instance.description = new_event.get(
                    "description", event_instance.description
                )
                event_instance.valid = new_event.get("valid", event_instance.valid)
                event_instance.save()

            # IF EVENT DOES NOT EXISTS, CREATE IT
            else:
                print("CREATE (event does not exist)")
                Event.objects.create(item=instance, **new_event)

        return instance
