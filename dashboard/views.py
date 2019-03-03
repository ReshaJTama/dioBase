from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

from .models import obatBase

from .forms import obatForm
from .forms import qtyForm

def index(request):
	obat = obatBase.objects.all()
	q = request.GET.get('q')
	if q is not None:
		obat = obat.filter(nameObat__icontains=q)
	else:
		obat = obatBase.objects.all()
	print(obat)
	context = {
		'obat':obat,
		'namespace':'tables.html'
		}
	return render(request,'dashboard/index.html',context)

def forms(request):
	form_data = obatForm(request.POST or None)
	if request.method == 'POST':
		if form_data.is_valid():
			obatBase.objects.create(
					nameObat = request.POST.get('nameObat'),
					qtyObat = request.POST.get('qtyObat'),
					kadaluarsaObat = request.POST.get('kadaluarsaObat'),
					categoryObat2 = request.POST.get('categoryObat2'),
					pic = request.POST.get('pic'),
				)
			return redirect('/dashboard')
		else:
			return HttpResponse('Barang Telah di input')
	context = {
		'forms':form_data,
	}
	return render(request,'dashboard/form.html',context)

def qtymasuk(request):
	form_data = qtyForm(request.POST or None)
	qtymas = request.POST.get('qtyObat')
	namemas = request.POST.get('nameObat')
	
	if request.method == 'POST':
		if form_data.is_valid():
			q = obatBase.objects.get(qtyObat__startswith=namemas).only(qtyObat)
			obatBase.objects.filter(
					nameObat__startswith = namemas
				).update(q)+qtymas
			return redirect('/dashboard')
		else:
			return HttpResponse('Barang telah di input')
	context = {
		'forms':form_data
	}
	return render(request,'dashboard/create.html',context)

def qtymasukForm(request,id):
	form_data = qtyForm2(request.POST or None)
	if request.method == 'POST':
		if form_data.is_valid():
			obatBase.objects.filter(qtymasuk).save(update_qtyObat=request.POST.get(qtyObat))

	return render(request,'dashboard/create.html',context)