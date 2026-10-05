from django.shortcuts import render
from django.http import HttpResponse

def items_view(request):
    return HttpResponse("items response")
