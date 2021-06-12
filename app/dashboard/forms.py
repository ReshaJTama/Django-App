from django import forms
from .models import List_sekolah
from .models import List_pendaftar

class SekolahForms(forms.ModelForm):
	class Meta:
		model = List_sekolah
		fields = "__all__"
		error_messages = {
			'npsn':{
				'required':"Anda harus mengisi IP Address"
			},
			'desc':{
				'required':"Anda harus mengisi Hostname"
			},
			'distrik':{
				'required':"Anda harus mengisi Departemen"
			},
			'status':{
				'required':"Anda harus mengisi status"
			},
			'telp':{
				'required':"Anda harus mengisi status"
			}
		}
		
class PendaftarForms(forms.ModelForm):
	class Meta:
		model = List_pendaftar
		fields = "__all__"
		