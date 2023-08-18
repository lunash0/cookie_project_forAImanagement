from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AccountsSerializer
from .models import Accounts

# Create your views here.
class AccountsViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()

'''
class CheckAccountViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

    def create(self, request):
        checkID = post_data['checkID']
        checkPW = post_data['checkPW']

        if Accounts.objects.filter(identify=checkID).exists():
            if Accounts.objects.filter(password=checkPW).exists():
                return Response(status=200)

        return Response(status=400)
'''