from django.db import models
from django.contrib.auth.models import User
import uuid
from pathlib import Path, PurePath
import os

from ne_sop_api.utils import Utils

# %% ENTITY TYPE
class EntityType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def __str__(self):
        return self.name


# %% ENTITY
class Entity(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    type = models.ForeignKey("EntityType", null=True, on_delete=models.SET_NULL)
    # type = models.CharField(choices=ENTITY_TYPES, default="", max_length=100)
    description = models.CharField(max_length=256, blank=True, default="")
    street = models.CharField(max_length=256, blank=True, default="")
    city = models.CharField(max_length=256, blank=True, default="")
    postalcode = models.CharField(max_length=25, blank=True, default="")
    region = models.CharField(max_length=256, blank=True, default="")
    country = models.CharField(max_length=100, blank=True, default="")
    website = models.URLField(max_length=512, blank=True, default="")
    email = models.EmailField(max_length=256, blank=True, default="")
    telephone = models.CharField(max_length=256, blank=True, default="")
    valid = models.BooleanField(default=True)
    # owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


# %% ITEM TYPE
class ItemType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# %% ITEM STATUS
class ItemStatus(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")
    color = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# %% ITEM
class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=30, blank=True, default="")
    title = models.CharField(max_length=512, blank=True, default="")

    author = models.ForeignKey(
        "Entity", related_name="author", null=True, on_delete=models.SET_NULL
    )

    type = models.ForeignKey("ItemType", null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey("ItemStatus", null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=600, blank=True, default="")
    urgent = models.BooleanField(default=False)
    writtenresponse = models.BooleanField(default=False)
    oralresponse = models.BooleanField(default=False)
    valid = models.BooleanField(default=True)

    lead = models.ForeignKey(
        "Entity",
        related_name="lead",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )
    support = models.ManyToManyField(Entity, blank=True, related_name="support")

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title


# %% EVENT TYPE
class EventType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# %% EVENT
class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField(null=True)
    item = models.ForeignKey(Item, related_name="events", on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=500, blank=True, default="")
    valid = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return str(self.date) + " - " + str(self.type)


class Template(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    item_types = models.ManyToManyField(ItemType)
    valid = models.BooleanField(default=True)
    relpath = models.CharField(default=None, max_length=400)

    class Meta:
        ordering = ["created"]

    @property
    def filename(self):
        return Path(self.relpath).name

    def __str__(self):
        return self.name


class NewDocument(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    template = models.ForeignKey(Template, null=True, on_delete=models.SET_NULL)
    note = models.CharField(max_length=500, blank=True, default="")
    filename = models.CharField(default=None, max_length=200)
    version = models.PositiveIntegerField(default=None)
    size = models.PositiveIntegerField(default=0, null=False)
    item = models.ForeignKey(Item, related_name="item_documents", on_delete=models.CASCADE)
    author = models.ForeignKey(Entity, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to=Utils.get_upload_path)

    class Meta:
        ordering = ["created"]

    @property
    def relpath(self):
        return PurePath(str(self.item.created.year), self.item.number, self.file.name)

    def __str__(self):
        return self.file.name


class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    template = models.ForeignKey(Template, null=True, on_delete=models.SET_NULL)
    note = models.CharField(max_length=500, blank=True, default="")
    valid = models.BooleanField(default=True)
    relpath = models.CharField(default=None, max_length=200)
    version = models.PositiveIntegerField(default=None)
    size = models.PositiveIntegerField(default=0, null=False)
    item = models.ForeignKey(Item, related_name="documents", on_delete=models.CASCADE)
    author = models.ForeignKey(Entity, null=True, on_delete=models.SET_NULL)
    # file = models.FileField()

    class Meta:
        ordering = ["created"]

    @property
    def filename(self):
        return Path(self.relpath).name
    
    @property
    def relpath(self):
        return PurePath(str(op.created.year), op.number)

    def __str__(self):
        return self.filename

