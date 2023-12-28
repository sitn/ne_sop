from ne_sop_api.models import (
    Document,
    Entity,
    EntityType,
    Event,
    EventType,
    Item,
    ItemStatus,
    ItemType,
    Template,
)
from ne_sop_api.serializers import (
    DocumentSerializer,
    EntitySerializer,
    EntityListSerializer,
    EntityTypeSerializer,
    NewItemSerializer,
    NestedItemSerializer,
    ItemListSerializer,
    ItemTypeSerializer,
    ItemStatusSerializer,
    EventSerializer,
    EventListSerializer,
    EventTypeSerializer,
    TemplateSerializer,
    UserSerializer,
)

from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import filters
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from ne_sop_api.utils import Utils
from ne_sop_api.permissions import (
    IsManagerPermission,
    IsManagerOrReadOnlyPermission,
    isAllowedRegadingEntitiesAndItemId
)

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
    permission_classes = [IsManagerPermission]

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
    permission_classes = [IsManagerOrReadOnlyPermission]

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


# ITEM SUMMARY
class ItemSummaryViewSet(viewsets.ViewSet):
    """
    Item summary viewset
    """

    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer
    search_fields = ["title", "number"]

    @extend_schema(
        tags=["Items"],
    )
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = NestedItemSerializer(item)
        return Response(serializer.data)


# ITEM
class ItemViewSet(viewsets.ViewSet):
    """
    Item viewset
    """

    serializer_class = NewItemSerializer
    search_fields = ["title", "number"]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Item.objects.all()
        return Item.objects.filter(support__in=user.entities.all())

    @extend_schema(
        responses=NewItemSerializer,
        tags=["Items"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, self.get_queryset(), self)

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
            item = serializer.save()
            Utils.itemCreatedNotification(item, request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = NewItemSerializer(item)
        return Response(serializer.data)

    @extend_schema(
        tags=["Items"],
    )
    def update(self, request, pk=None):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = NewItemSerializer(item, data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            if item.autonotify is True:
                Utils.itemChangedNotification(item, request)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.get_queryset(), pk=pk)
        item.delete()
        Utils.itemRemovedNotification(item, request)
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

    serializer_class = EventSerializer
    search_fields = ["date", "item__number", "item__title"]
    permission_classes = [IsManagerOrReadOnlyPermission]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(item__support__in=user.entities.all())

    @extend_schema(
        responses=EventSerializer,
        tags=["Events"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, self.get_queryset(), self)

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

        if item and len(item) > 0:
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
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @extend_schema(
        tags=["Events"],
    )
    def update(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Events"],
    )
    def destroy(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        event.delete()
        return Response({"msg": "Event deleted"})


# %% TEMPLATE
class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Templates viewset
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


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
class DocumentViewSet(viewsets.ViewSet):
    """
    New document viewset
    """
    parser_classes = [MultiPartParser]
    serializer_class = DocumentSerializer

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(item__support__in=user.entities.all())

    @extend_schema(
        responses=DocumentSerializer,
        tags=["Document"],
    )
    def create(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses=DocumentSerializer,
        tags=["Document"],
    )
    def retrieve(self, request, pk):
        document = get_object_or_404(self.get_queryset(), pk=pk)

        filepath = PurePath(settings.MEDIA_ROOT, document.file.name)
        filepath = open(filepath, "rb")
        
        response = FileResponse(
            filepath, filename=document.filename, as_attachment=True
        )

        headers = response.headers
        headers["Content-Type"] = "application/download"
        headers["Accept-Ranges"] = "bite"
        response["Content-Disposition"] = f"attachment; filename={document.filename}"
        return response

    @extend_schema(
        responses=DocumentSerializer,
        tags=["Document"],
    )
    def destroy(self, request, pk=None):
        document = get_object_or_404(self.get_queryset(), pk=pk)
        os.remove(PurePath(settings.MEDIA_ROOT, document.file.name))
        document.delete()
        return Response({"msg": "Document deleted"})


# %% TEST BACKEND
@api_view(["GET"])
def notificationNewItem(request, item_id):
    """
    Send mail for new items
    """
    item = get_object_or_404(Item.objects.all(), pk=item_id)

    response_html = Utils.itemChangedNotification(item, request)

    # msg = EmailMultiAlternatives(
    #     subject=f"SOP - modification de l'op {item.id}",
    #     body=response_html,
    #     from_email="noreply-sop@ne.ch",
    #     to=["marc.rufener@ne.ch"],
    #     # cc=["matthew.parkan@ne.ch", "stephane.maltaesousa@ne.ch"],
    # )

    # msg.content_subtype="html"
    # msg.send()

    return HttpResponse(response_html)
