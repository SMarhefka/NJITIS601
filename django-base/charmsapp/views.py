from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Creating an index view...this is the initial view when 
# the user types in localhost:8000/charmsapp/
# This view will be where the excel file is uploaded
def index(request):
    return HttpResponse("I am in the index view");
