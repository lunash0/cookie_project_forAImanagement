from rest_framework import serializers
from .models import Accounts, Pet, Walk, Breed

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['USER_ID', 'PASSWORD']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['PET_ID', 'PET_NAME', 'PET_GENDER', 'PET_NEUTER', 'PET_BIRTH', 'PET_BREED', 'WALK_TIME', 'WALK_PLACE']

class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = ['WALK_PLACE', 'WALK_METHOD']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['PET_BREED', 'PET_METHOD']