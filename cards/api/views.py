from ..models import flash_card
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class flash_cardListView(generics.ListAPIView):
    """ To View all cards and their Questions and Answer Fields"""
    queryset = flash_card.objects.all()
    template_name='views.html'
    serializer_class = serializers.Flash_cardSerializer



class flash_cardCreateView(generics.CreateAPIView):
    queryset = flash_card.objects.all()
    serializer_class = serializers.Flash_cardSerializer

    def create(self, request, *args, **kwargs):
        super(flash_cardCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


class flash_cardDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Answer View"""
    queryset = flash_card.objects.all()
    serializer_class = serializers.Flash_cardSerializer
    
    def retrieve(self, request, *args, **kwargs):
        super(flash_cardDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": data}

        return Response(response['result']['answer'])


    def patch(self, request, *args, **kwargs):
        super(flash_cardDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": data}
        return Response(response)


    def delete(self, request, *args, **kwargs):
        super(flash_cardDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created"}
        return Response(response)

 
