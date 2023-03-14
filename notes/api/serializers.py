from rest_framework import serializers
# from rest_framework import users # remove this
from .models import Notes # add this


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        # model = get_user_model() # this will work too
        fields = '__all__'
