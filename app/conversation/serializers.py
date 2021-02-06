
from rest_framework import serializers
from . models import Conversation

def positive(value):
    if value <= 0:
        raise serializers.ValidationError('User id is not positive')

class StartConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = ['language']

class KeepConversationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(validators=[positive])
    message = serializers.CharField(max_length=255, allow_blank=False, trim_whitespace=True)