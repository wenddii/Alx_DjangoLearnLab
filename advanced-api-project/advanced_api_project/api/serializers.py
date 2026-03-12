from rest_framework import serializers
from .models import Author,Book
from .serializers import MethodField

class AuhtorSerializer(serializers.ModelSerializer):
    book = BookSerializer.SerializersMethodField()
    class Meta():
        model = Author
        fields = ['name','book']
class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields ='__all__'
    def validate(self, attrs):
        if publication_year > current_date validationError("publication year invalid")
        return BookSerializer


