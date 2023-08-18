from django.db import models

class Accounts(models.Model):
    USER_ID = models.CharField(default='USER_ID', max_length=20, primary_key=True)
    PASSWORD = models.CharField(default='PASSWORD', max_length=20)


class Walk(models.Model):
    WALK_PLACE = models.CharField(max_length=50, primary_key=True)
    WALK_METHOD = models.CharField(max_length=100)

class Breed(models.Model):
    PET_BREED = models.CharField(max_length=50, primary_key=True)
    PET_METHOD = models.CharField(max_length=100)
    
class Pet(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    YES_NO_CHOICES = [('Y', 'Yes'), ('N', 'No')]
    
    PET_ID = models.AutoField(primary_key=True)
    PET_NAME = models.CharField(max_length=50)
    PET_GENDER = models.CharField(max_length=1, choices=GENDER_CHOICES)
    PET_NEUTER = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    PET_BIRTH = models.DateField()
    PET_BREED = models.OneToOneField(Breed, on_delete=models.CASCADE)
    WALK_TIME = models.CharField(max_length=50)
    WALK_PLACE = models.OneToOneField(Walk, on_delete=models.CASCADE)

class SkinInfo(models.Model):
    PET_ID = models.OneToOneField(Pet, on_delete=models.CASCADE, primary_key=True)
    SKIN_TYPE = models.CharField(max_length=20)
    THERAPY = models.CharField(max_length=100)

class User(models.Model):
    USER_ID = models.OneToOneField(Accounts, on_delete=models.CASCADE, primary_key=True)
    USER_NAME = models.CharField(max_length=80)
    PET_ID = models.OneToOneField(Pet, on_delete=models.CASCADE, unique=True)

# Create your models here.
