from rest_framework import serializers
from .models import Text,Author,Stats



class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = ('slowo',)
        # fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('imie',)
        # fields = '__all__'

class StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stats
        fields = ('slowo','liczebnosc',)

