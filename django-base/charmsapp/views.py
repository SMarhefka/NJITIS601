from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
import openpyxl

from django.contrib import messages
from django.urls import reverse
from .resources import SampleDataResource
from tablib import Dataset
from .models import SampleData
from .tables import SampleDataTable

# Create your views here.
# Creating an index view...this is the initial view when 
# the user types in localhost:8000/charmsapp/
# This view will be where the excel file is uploaded
def index(request):
    if "GET" == request.method:
        return render(request, 'charmsapp/index.html', {})
        

# This is the upload view
# # the user types in localhost:8000/charmsapp/upload
def upload(request):
    if "GET" == request.method:
        return render(request, 'charmsapp/upload.html', {})
    else:
        sample_resource = SampleDataResource()
        dataset = Dataset()

        excel_file = ""
        excel_file = request.FILES["excel_file"]

        # error check to make sure the file is an excel file
        if not excel_file.name.endswith('xlsx'):
            messages.info(request, 'File has the wrong format, must be an xlsx file!')
            return render(request, 'charmsapp/upload.html', {})

        # Loads an excel file
        imported_data = dataset.load(excel_file.read(), format='xlsx')
        #print (imported_data)
        count=0
        for data in imported_data:
        	# print(data[1])
        	value = SampleData(
                first_name = data[0],
                last_name = data[1],
                email = data[2],
                fav_number = data[3],
                sample_date = data[4],
        		)
        	value.save()  

        """
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        #print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        #print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        #print(active_sheet)

        # reading a cell
        #print(worksheet["A2"].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        #for row in worksheet.iter_rows():
        #    row_data = list()
        #    for cell in row:
        #        row_data.append(str(cell.value))
        #        print(cell.value)
        #    excel_data.append(row_data)
        """
        return render(request, 'charmsapp/upload.html', {"excel_data":imported_data})

def view_data(request):
    if "GET" == request.method:
        # return HttpResponse("GET REQUEST: This is the view/review page");
        #sample_data = SampleDataTable(SampleData.objects.all())
        #RequestConfig(request).configure(sample_data)
        sample_data = SampleData.objects.all()
        return render(request, "charmsapp/review.html", {
            'test_data':sample_data
        })
    else:
        return HttpResponse("POST REQUEST: This is the view/review page");
