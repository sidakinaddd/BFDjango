from rest_framework import serializers
from .models import Journal, Book

class BookSerializer(serializers.ModelSerializer):
    # num_pages = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book
        fields = ('__all__')

    def validated_page(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of pages should be more than 0")
        return value


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('__all__')

        def validated_type(self, value):
            if value != 'Bullet' or value != 'Food' or value != 'Travel' or value!='Sport':
                raise serializers.ValidationError(" Not a classic type")
            return value