from django import forms
from django.forms import DateInput
from .models import obatBase,AppModels


class obatForm(forms.ModelForm):
	class Meta:
		model = obatBase
		fields = [
				'nameObat',
				'qtyObat',
				'kadaluarsaObat',
				'categoryObat2',
				'pic'
		]
		widgets = {

			'categoryObat2': forms.Select(attrs={'class':'form-control form-control-user'}),
			'nameObat': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
			'qtyObat': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
			'picObat': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
			'kadaluarsaObat': forms.DateInput(attrs={'class': 'form-control form-control-user', 'id':'datepicker'}),
		}


class qtyForm(forms.ModelForm):
	class Meta:
		model= obatBase
		fields = [
			'nameObat',
			'qtyObat',
		]


class qtyFormexam(forms.ModelForm):
	class Meta:
		model  = AppModels
		fields = [
			'Choices',
		]
		widgets={
			'Choices': forms.Select(attrs={'class':'form-control form-control-user'}),
		}

class qtyForm2(forms.ModelForm):
	class Meta:
		model  = obatBase
		fields = [
			'qtyObat',
		]
		widgets={
			'qtyObat': forms.NumberInput(attrs={'class':'form-control form-control-user'}),
		}