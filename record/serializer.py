
# coding: utf-8
from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('date', 'name', 'tool', 'num', 'skill', 'count', 'publishing',)
