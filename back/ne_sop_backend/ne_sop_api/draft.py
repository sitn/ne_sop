# from django.shortcuts import render
from ne_sop_api.models import Entity, Item, Event
from ne_sop_api.serializers import EntitySerializer, ItemSerializer
from django.shortcuts import get_object_or_404

# from rest_framework import generics
from rest_framework import viewsets

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from drf_spectacular.utils import extend_schema


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "entities": reverse("entity-list", request=request, format=format),
            # "items": reverse("item-list", request=request, format=format),
        }
    )


# %% Create your views here.


class EntityList(APIView):
    """
    List all entities, or create a new entity.
    """

    def get(self, request, format=None):
        entities = Entity.objects.all()
        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntityDetail(APIView):
    """
    Retrieve, update or delete an entity instance.
    """

    def get_object(self, pk):
        try:
            return Entity.objects.get(pk=pk)
        except Entity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EntitySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EntitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
