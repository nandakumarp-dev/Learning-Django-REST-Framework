from rest_framework import serializers

from .models import Books

class BooksSerializer(serializers.ModelSerializer):

    class Meta:

        model = Books

        fields = '__all__'

        # exclude = ['active_status','uuid']

        read_only_fields = ['active_status','uuid']

