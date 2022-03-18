from rest_framework import serializers
from .models import Feeds

class simple_feed_ser(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = '__all__'