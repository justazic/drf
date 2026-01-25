from django.shortcuts import render,get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import House
from .serializers import HouseSerializer


class HouseListCreateAPIView(GenericAPIView):
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(House.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class HouseDetailAPIView(GenericAPIView):
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(House, pk=pk)

    def get(self, request, pk):
        serializer = self.serializer_class(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.serializer_class(
            self.get_object(pk),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)