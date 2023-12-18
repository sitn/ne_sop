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
    User,
)
from ne_sop_api.serializers import (
    DocumentByItemSerializer,
    EntitySerializer,
    EntityListSerializer,
    EntityTypeSerializer,
    FileSerializer,
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
from rest_framework.parsers import MultiPartParser
from rest_framework import filters
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse

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
        if sortby not in ["id", "number", "title", "type", "status", "urgent"]:
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


class DocumentViewSet(viewsets.ViewSet):
    """
    Documents viewset
    """

    queryset = Document.objects.all()
    # serializer_class = DocumentByItemSerializer

    @extend_schema(
        responses=DocumentByItemSerializer,
        tags=["Documents"],
    )
    def list(self, request):
        item_id = request.query_params.get('item_id') if 'item_id' in request.query_params else None

        documents = Document.objects
        if item_id is not None:
            documents = documents.filter(item_id=item_id)
        documents = documents.all().order_by('template', '-version')

        serializer = DocumentByItemSerializer(documents, many=True)
        return Response(serializer.data)


    @extend_schema(
        tags=["Documents"],
    )
    def destroy(self, request, pk=None):
        document = get_object_or_404(self.queryset, pk=pk)

        root_dir = os.environ['NESOP_OP_PATH']
        filepath = Path( PurePath(root_dir, document.relpath) )
        if filepath.exists():
            os.remove(filepath)

        document.delete()
        return Response({"msg": "Document deleted"})


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
        itemtype_id = request.query_params.get('itemtype_id') if 'itemtype_id' in request.query_params else None
    
        templates = Template.objects
        if itemtype_id is not None:
            templates = templates.filter(item_types__id=itemtype_id)
        templates = templates.all()

        serializer = TemplateSerializer(templates, many=True)
        
        return Response(serializer.data)


class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser]

    @extend_schema(
        responses=FileSerializer,
        tags=["Documents"],
    )
    def post(self, request, filename):
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        file_obj = request.FILES['file']
        item_id = request.data['item_id'] if 'item_id' in request.data else None
        template_id = request.data['template_id'] if 'template_id' in request.data else None
        note = request.data['note'] if 'note' in request.data else None
        size = request.data['size'] if 'size' in request.data else None
        author_id = request.data['author_id'] if 'author_id' in request.data else None

        documents = Document.objects.filter(
            item=item_id,
            template=template_id
        ).all().order_by("-version")
        
        version = 1
        if len(documents) > 0:
            version = documents[0].version + 1

        file_extension = filename.rsplit('.', 1)[1]

        if int(template_id) != int( os.environ['NESOP_TEMPLATE_AUTRE_ID'] ):
            template = Template.objects.filter(id=template_id).first()
            filename = template.filename

        filename = filename.rsplit('.', 1)[0] + f'_v{version}.' + file_extension

        root_dir = os.environ['NESOP_OP_PATH']
        op = Item.objects.filter(id=item_id).first()
        relpath = PurePath(str(op.created.year), op.number, filename)
        filepath = PurePath(root_dir, relpath)

        filepath = Utils.iterateFilename(filepath)

        if not os.path.exists(Path(filepath).resolve().parent):
            os.makedirs(Path(filepath).resolve().parent)

        with open(filepath, 'wb') as output_file:
            shutil.copyfileobj(file_obj.file, output_file)


        document = Document()
        document.template_id = template_id
        document.note = note
        document.relpath = relpath
        document.version = version
        document.item_id = item_id
        document.size = size
        document.author_id = author_id

        document.save()

        return Response({"msg": "Document created"}, status=status.HTTP_201_CREATED)

class FileDownloadView(views.APIView):

    queryset = Document.objects.all()

    @extend_schema(
        tags=["Documents"],
    )
    def get(self, request, pk=None, format=None):
        print('pk =', pk)
        document = get_object_or_404(self.queryset, pk=pk)

        root_dir = os.environ['NESOP_OP_PATH']
        filepath = PurePath(root_dir, document.relpath)
        print('filepath = ', filepath)
        filepath = open(filepath, 'rb')

        response = FileResponse(filepath, filename=document.filename, as_attachment=True)
        headers = response.headers
        headers['Content-Type'] = 'application/download'
        headers['Accept-Ranges'] = 'bite'
        response['Content-Disposition'] = f'attachment; filename={document.filename}'
        return response
