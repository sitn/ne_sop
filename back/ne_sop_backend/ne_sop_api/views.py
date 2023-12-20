from ne_sop_api.models import (
    NewDocument,
    Entity,
    EntityType,
    Event,
    EventType,
    Item,
    ItemStatus,
    ItemType,
    Template,
    User,
)
from ne_sop_api.serializers import (
    # DocumentSerializer,
    NewDocumentSerializer,
    EntitySerializer,
    EntityListSerializer,
    EntityTypeSerializer,
    NewItemSerializer,
    ItemListSerializer,
    ItemTypeSerializer,
    ItemStatusSerializer,
    EventSerializer,
    EventListSerializer,
    EventTypeSerializer,
    TemplateSerializer,
    UserSerializer,
)

from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import filters
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse

from django.conf import settings

from ne_sop_api.utils import Utils

from pathlib import Path, PurePath
import os
import shutil


# %% TEST BACKEND
@api_view(["GET"])
def test_api(request):
    """
    Test backend
    """
    html = "<h1>Congratulations !</h1>"
    html += f"<h2>Hello {request.user}, It works</h2>"
    return HttpResponse(content=html, status=200)


# %% USER
class UserViewSet(viewsets.ViewSet):
    """
    Users viewset
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        responses=UserSerializer,
        tags=["Users"],
    )
    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% ENTITY TYPE
class EntityTypeViewSet(viewsets.ViewSet):
    """
    Entity types viewset
    """

    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer

    @extend_schema(
        responses=EntityTypeSerializer,
        tags=["Entity type"],
    )
    def list(self, request):
        serializer = EntityTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% ENTITY
class EntityViewSet(viewsets.ViewSet):
    """
    Entities viewset
    """

    serializer_class = EntitySerializer
    search_fields = ["name", "email", "telephone"]

    @extend_schema(
        tags=["Entities"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, Entity.objects.all(), self)

        # queryset = Entity.objects.all()
        name = request.query_params.get("name", "")
        type = request.query_params.get("type")
        page = int(request.query_params.get("page", "1"))
        size = int(request.query_params.get("size", "10"))
        sortby = request.query_params.get("sortby", "id")
        descending = request.query_params.get("descending", "false")
        # all_fields = Entity._meta.fields

        if sortby not in ["id", "name", "type"]:
            sortby = "id"

        if descending not in ["true", "false"]:
            descending = "false"

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        if type:
            queryset = queryset.filter(type__in=type.split(","))

        if descending == "true":
            paginator = Paginator(queryset.order_by(Lower(sortby).desc()), size)
        else:
            paginator = Paginator(queryset.order_by(Lower(sortby).asc()), size)

        queryset = paginator.page(page)
        nrows = paginator.count
        npages = paginator.num_pages

        serializer = EntityListSerializer(queryset, many=True)

        return Response(
            {
                "page": page,
                "npages": npages,
                "nrows": nrows,
                "sortby": sortby,
                "descending": descending,
                "results": serializer.data,
            }
        )

    @extend_schema(
        tags=["Entities"],
    )
    def create(self, request):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({"msg": "New entity created"}, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Entities"],
    )
    def retrieve(self, request, pk=None):
        queryset = Entity.objects.all()
        entity = get_object_or_404(queryset, pk=pk)
        serializer = EntitySerializer(entity)
        return Response(serializer.data)

    @extend_schema(
        tags=["Entities"],
    )
    def update(self, request, pk=None):
        queryset = Entity.objects.all()
        entity = get_object_or_404(queryset, pk=pk)
        serializer = EntitySerializer(entity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Entities"],
    )
    def destroy(self, request, pk=None):
        queryset = Entity.objects.all()
        entity = get_object_or_404(queryset, pk=pk)
        entity.delete()
        return Response({"msg": "Entity deleted"})


# %% ITEM TYPE
class ItemTypeViewSet(viewsets.ViewSet):
    """
    Item types viewset
    """

    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer

    @extend_schema(
        responses=ItemTypeSerializer,
        tags=["Item types"],
    )
    def list(self, request):
        serializer = ItemTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% ITEM STATUS
class ItemStatusViewSet(viewsets.ViewSet):
    """
    Item status viewset
    """

    queryset = ItemStatus.objects.all()
    serializer_class = ItemStatusSerializer

    @extend_schema(
        responses=ItemStatusSerializer,
        tags=["Item status"],
    )
    def list(self, request):
        serializer = ItemStatusSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ItemViewSet(viewsets.ViewSet):
    """
    Item viewset
    """

    queryset = Item.objects.all()
    serializer_class = NewItemSerializer
    search_fields = ["title", "number"]

    @extend_schema(
        responses=NewItemSerializer,
        tags=["Items"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, Item.objects.all(), self)

        title = request.query_params.get("title", "")
        number = request.query_params.get("number", "")
        page = int(request.query_params.get("page", "1"))
        size = int(request.query_params.get("size", "10"))
        sortby = request.query_params.get("sortby", "id")
        descending = request.query_params.get("descending", "false")

        # all_fields = Entity._meta.fields
        if sortby not in [
            "id",
            "number",
            "title",
            "type",
            "status",
            "urgent",
            "startdate",
            "enddate",
        ]:
            sortby = "id"

        if descending not in ["true", "false"]:
            descending = "false"

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        if number is not None:
            queryset = queryset.filter(number__icontains=number)

        if descending == "true":
            paginator = Paginator(queryset.order_by(Lower(sortby).desc()), size)
        else:
            paginator = Paginator(queryset.order_by(Lower(sortby).asc()), size)

        queryset = paginator.page(page)
        nrows = paginator.count
        npages = paginator.num_pages

        serializer = ItemListSerializer(queryset, many=True)

        # return Response(serializer.data)
        return Response(
            {
                "page": page,
                "npages": npages,
                "nrows": nrows,
                "sortby": sortby,
                "descending": descending,
                "results": serializer.data,
            }
        )

    @extend_schema(
        tags=["Items"],
    )
    def create(self, request):
        serializer = NewItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({"msg": "Item created"}, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = NewItemSerializer(item)
        return Response(serializer.data)

    @extend_schema(
        tags=["Items"],
    )
    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = NewItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response({"msg": "Item deleted"})


# %% EVENT TYPE
class EventTypeViewSet(viewsets.ViewSet):
    """
    Event types viewset
    """

    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

    @extend_schema(
        responses=EventTypeSerializer,
        tags=["Event types"],
    )
    def list(self, request):
        serializer = EventTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% EVENT
class EventViewSet(viewsets.ViewSet):
    """
    Events viewset
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    search_fields = ["date", "item__number", "item__title"]

    @extend_schema(
        responses=EventSerializer,
        tags=["Events"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, Event.objects.all(), self)

        # queryset = Event.objects.all()
        item = request.query_params.get("item", None)
        page = int(request.query_params.get("page", "1"))
        size = int(request.query_params.get("size", "10"))
        sortby = request.query_params.get("sortby", "id")
        descending = request.query_params.get("descending", "false")

        if sortby not in ["id", "date", "type", "item"]:
            sortby = "id"

        if descending not in ["true", "false"]:
            descending = "false"

        if len(item):
            queryset = queryset.filter(item__exact=item)

        if descending == "true":
            paginator = Paginator(queryset.order_by(Lower(sortby).desc()), size)
        else:
            paginator = Paginator(queryset.order_by(Lower(sortby).asc()), size)

        queryset = paginator.page(page)
        nrows = paginator.count
        npages = paginator.num_pages

        serializer = EventListSerializer(queryset, many=True)

        return Response(
            {
                "page": page,
                "npages": npages,
                "nrows": nrows,
                "sortby": sortby,
                "descending": descending,
                "results": serializer.data,
            }
        )

    @extend_schema(
        tags=["Events"],
    )
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Event created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Events"],
    )
    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @extend_schema(
        tags=["Events"],
    )
    def update(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Events"],
    )
    def destroy(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        event.delete()
        return Response({"msg": "Event deleted"})


# %% TEMPLATE
class TemplateViewSet(viewsets.ViewSet):
    """
    Templates viewset
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @extend_schema(
        responses=TemplateSerializer,
        tags=["Templates"],
    )
    def list(self, request):
        serializer = TemplateSerializer(self.queryset, many=True)
        return Response(serializer.data)


class TemplateTypeViewSet(viewsets.ViewSet):
    """
    Template types viewset
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @extend_schema(
        responses=TemplateSerializer,
        tags=["Template type"],
    )
    def list(self, request):
        itemtype_id = (
            request.query_params.get("itemtype_id")
            if "itemtype_id" in request.query_params
            else None
        )

        templates = Template.objects
        if itemtype_id is not None:
            templates = templates.filter(item_types__id=itemtype_id)
        templates = templates.all()

        serializer = TemplateSerializer(templates, many=True)

        return Response(serializer.data)

# from pprint import pprint
class NewDocumentViewSet(viewsets.ViewSet):
    """
    New document viewset
    """
    parser_classes = [MultiPartParser]

    queryset = NewDocument.objects.all()
    serializer_class = NewDocument

    @extend_schema(
        responses=NewDocumentSerializer,
        tags=["NewDocument"],
    )
    def create(self, request):
        serializer = NewDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses=NewDocumentSerializer,
        tags=["NewDocument"],
    )
    def retrieve(self, request, pk):
        document = get_object_or_404(self.queryset, pk=pk)
        serializer = NewDocumentSerializer(document)
        return Response(serializer.data)
    
    @extend_schema(
        responses=NewDocumentSerializer,
        tags=["NewDocument"],
    )
    def destroy(self, request, pk=None):
        document = get_object_or_404(self.queryset, pk=pk)
        print('document', document)
        os.remove(PurePath(settings.MEDIA_ROOT, document.file.name))
        document.delete()
        return Response({"msg": "Document deleted"})
