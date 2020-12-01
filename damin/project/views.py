from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

def dashboard(request):
	return render(request, "project/dashboard.html", {})

def proses(request):
	return render(request, "project/proses.html", {})

def desc(request):
	return render(request, "project/desc.html", {})

def table(request):
	return render(request, "project/table.html", {})

def visualisasi(request):
	return render(request, "project/visualisasi.html", {})

def data(request):
	return render(request, "project/data.html", {})
