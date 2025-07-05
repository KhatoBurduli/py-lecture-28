from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer


# Create your views here.
class SelectBooksView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data = Book.objects.get(pk=pk)
                serializer = BookSerializer(data, context={"request":request},many=False)
                return Response(serializer.data)
            except:
                return Response("Could not find a book with id = "+str(pk))
        data = Book.objects.all()
        serializer = BookSerializer(data, context={"request":request}, many=True)
        return Response(serializer.data)


class AddBookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteBookView(APIView):
    def delete(self, request, pk):
        event = Book.objects.get(pk=pk)
        event.delete()
        return Response("Deletion successful")