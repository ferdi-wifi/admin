from django import forms
from surat_menyurat.models import Disposisi_keluar, Instansi, SuratMasuk, SuratKeluar, Struktural, Disposisi
from django.forms import ModelForm
from django.contrib.auth.models import User

class FormSuratMasuk(forms.ModelForm):
  class Meta:
    model = SuratMasuk
    exclude = ('id', )

  def __init__(self, *args, **kwargs):
    super(FormSuratMasuk, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'
    
class FormSuratKeluar(forms.ModelForm):
  class Meta:
    model = SuratKeluar
    exclude = ('id', )

  def __init__(self, *args, **kwargs):
    super(FormSuratKeluar, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'
      
class FormInstansi(forms.ModelForm):
  class Meta:
    model = Instansi
    exclude = ('id', )

  def __init__(self, *args, **kwargs):
    super(FormInstansi, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'


class StrukturalForm(ModelForm):
    class Meta:
        model = Struktural
        fields=['nama','jabatan','alamat','email']
    def __init__(self, *args, **kwargs):
      super(StrukturalForm, self).__init__(*args, **kwargs)
      for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control'
       
class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['username']
        help_texts ={
            'username':''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':'required'}),
        }
        labels = {
            'username': 'Username*',
        }


class FormDiposisi(forms.ModelForm):
  class Meta:
    model = Disposisi
    exclude = ('id','suratmasuk')

  def __init__(self, *args, **kwargs):
    super(FormDiposisi, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'

class FormDiposisiKeluar(forms.ModelForm):
  class Meta:
    model = Disposisi_keluar
    exclude = ('id','suratkeluar')

  def __init__(self, *args, **kwargs):
    super(FormDiposisiKeluar, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'