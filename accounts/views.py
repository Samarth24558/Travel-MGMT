from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
	return render(request, 'accounts/index.html')

def insert(request):
	form = InsertForm()
	if request.method == 'POST':
		form = InsertForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/insert_list')
	context={'form':form}
	return render(request, 'accounts/insert.html',context)


def insert_list(request):
	list =Insert.objects.all()
	context={'list':list}
	return render(request, 'accounts/insert_list.html',context)



def party_gc(request):
	form = Party_gcForm()
	if request.method == 'POST':
		form = Party_gcForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/all_gc_list')
	context={'form':form}
	return render(request, 'accounts/party_gc.html',context)


def all_gc_list(request):
	list =Party_gc.objects.all()
	context={'list':list}
	return render(request, 'accounts/all_gc_list.html',context)



def consignor_insert(request):
	form = ConsignorForm()
	if request.method == 'POST':
		form = ConsignorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/consignor_list')
	context={'form':form}
	return render(request, 'accounts/consignor_insert.html',context)


def consignor_list(request):
	list =Consignor.objects.all()
	context={'list':list}
	return render(request, 'accounts/consignor_list.html',context)



def consignee_insert(request):
	form = ConsigneeForm()
	if request.method == 'POST':
		form = ConsigneeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/consignee_list')
	context={'form':form}
	return render(request, 'accounts/consignee_insert.html',context)


def consignee_list(request):
	list =Consignee.objects.all()
	context={'list':list}
	return render(request, 'accounts/consignee_list.html',context)