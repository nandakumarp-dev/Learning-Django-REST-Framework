from rest_framework import serializers

from .models import Singers

class SingersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Singers

        fields = '__all__'

        # exclude = ['active_status','uuid']

        read_only_fields = ['active_status','uuid']

