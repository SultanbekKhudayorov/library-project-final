from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {'title': 'Title must be alphanumeric'}
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {'title': 'Title can only be unique'}
            )

        return data

    def validate_price(self, price):
        if price <= 0 or price > 1000000000:
            raise ValidationError(
                {'price': 'Price must be between 0 and 100000000'}
            )