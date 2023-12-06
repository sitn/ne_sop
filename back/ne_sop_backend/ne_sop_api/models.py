from django.db import models
from django.contrib.auth.models import User
import uuid

ENTITY_TYPES = [
    ("SERVICE_ETAT", "Service de l'état"),
    ("PARLEMENTAIRE", "Parlementaire"),
    ("GROUPE_PARLEMENTAIRE", "Groupe parlementaire"),
    ("AUTRE", "Autre"),
]


ITEM_TYPES = [
    ("INTERPELLATION", "Interpellation"),
    ("MOTION", "Motion"),
    ("POSTULAT", "Postulat"),
    ("PROJET_LOIS", "Projet de lois et décrets"),
    ("QUESTION", "Question"),
    ("RAPPORT", "Rapport"),
    ("RECOMMANDATION", "Recommandation"),
    ("RESOLUTION", "Resolution"),
]

EVENT_TYPES = []


class ItemTypes(models.TextChoices):
    INTERPELLATION = "Interpellation", "Interpellation"
    MOTION = "Motion", "Motion"


# %%


class EntityType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def __str__(self):
        return self.name


# Create your models here.
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


class ItemType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ItemStatus(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")
    color = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=30, blank=True, default="")
    title = models.CharField(max_length=512, blank=True, default="")

    author = models.ForeignKey(
        "Entity", related_name="author", null=True, on_delete=models.SET_NULL
    )

    # type = models.CharField(choices=ITEM_TYPES, default="", max_length=100)
    type = models.ForeignKey("ItemType", null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey("ItemStatus", null=True, on_delete=models.SET_NULL)
    # events = models.ForeignKey("Event", many=True, null=True, on_delete=models.SET_NULL)
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


class EventType(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    item = models.ForeignKey(Item, related_name="events", on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=500, blank=True, default="")
    valid = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.date


class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    date = models.DateField()
    note = models.CharField(max_length=500, blank=True, default="")
    valid = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.date


class Template(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    parents = models.ManyToManyField(ItemType)
    valid = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.name


"""
from ne_sop_api.models import Entity

Entity.objects.create(
    name="Service de l'aménagement du territoire (SCAT)",
    type="Service de l'état",
    description="",
    street="Rue de Tivoli 5",
    city="Neuchâtel",
    postalcode="2002",
    region="Neuchâtel",
    country="Suisse",
    website="",
    email="Service.AmenagementTerritoire@ne.ch",
    telephone="+41 32 889 67 40",
    valid=True,
)

Entity.objects.create(
    name="Service de la faune, des forêts et de la nature (SFFN)",
    type="Service de l'état",
    description="",
    street="Rue du Premier-Mars 11",
    city="Couvet",
    postalcode="2108",
    region="Neuchâtel",
    country="Suisse",
    website="",
    email="SFFN@ne.ch",
    telephone="+41 32 889 67 60",
    valid=True,
)


Entity.objects.all()

"""
