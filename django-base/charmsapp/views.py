from django.shortcuts import render
from django.http import HttpResponse

import openpyxl

# Create your views here.
# Creating an index view...this is the initial view when 
# the user types in localhost:8000/charmsapp/
# This view will be where the excel file is uploaded
def index(request):
    return HttpResponse("I am in the index view");

# This is the upload view
# # the user types in localhost:8000/charmsapp/upload
def upload(request):
    if "GET" == request.method:
        return render(request, 'charmsapp/upload.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        print(active_sheet)

        # reading a cell
        print(worksheet["A1"].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(cell.value)
            excel_data.append(row_data)

        return render(request, 'charmsapp/upload.html', {"excel_data":excel_data})
