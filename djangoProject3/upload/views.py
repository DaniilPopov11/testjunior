from django.shortcuts import render
from django.http import HttpResponse


def upload(request):
    return render(request, 'upload/csv.html')
