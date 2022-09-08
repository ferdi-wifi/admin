import xlwt
from django.shortcuts import render, redirect, get_object_or_404

from .models import SuratMasuk, SuratKeluar, Instansi, Struktural, Disposisi, Disposisi_keluar
from .forms import FormSuratMasuk, FormInstansi, FormSuratKeluar,StrukturalForm,UserForm,FormDiposisi, FormDiposisiKeluar
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .decorators import tolakhalaman_ini, ijinkan_pengguna,pilihan_login
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from django.http import HttpResponse

@login_required(login_url='login_page')
@pilihan_login
def home(request):
      jmlSuratMasuk = SuratMasuk.objects.all().count()
      jmlSuratKeluar = SuratKeluar.objects.all().count()
      jmlInstansi = Instansi.objects.all().count()
      jmlStruktural = Struktural.objects.all().count()
      jmlDisposisi = Disposisi.objects.all().count()
      jmlDisposisikeluar = Disposisi_keluar.objects.all().count()

    
      context={
        'judul':'Halaman Beranda',
        'menu':'beranda',
        'jmlSuratMasuk':jmlSuratMasuk,
        'jmlSuratKeluar':jmlSuratKeluar,
        'jmlInstansi':jmlInstansi,
        'jmlStruktural':jmlStruktural,
        'jmlDisposisi':jmlDisposisi,
        'jmlDisposisikeluar':jmlDisposisikeluar,


      }
      return render(request, 'home.html', context)


@tolakhalaman_ini
def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    cocokan = authenticate(request, username=username, password=password)
    if cocokan is None:
      messages.error(request, 'Usernama dan Password salah')
      return redirect('login_page')
        
    if cocokan is not None:
        login(request, cocokan)
        return redirect('home')
  context = {
        'judul': 'Halaman Login',
        'menu': 'login',
  }
  return render(request, "registration/login.html",context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_masuk_list(request):
  data= SuratMasuk.objects.all().order_by('-id')
  context={
     'judul':'Halaman List Surat Masuk',
    'menu':'masuk',
    'data':data

  }
  return render(request, "surat/surat_masuk_list.html",context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_masuk_delete(request, id):
  surat_masuk = get_object_or_404(SuratMasuk, pk=id)
  surat_masuk.delete()
  return redirect('surat:surat_masuk_list')

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_masuk_edit(r, id):
  if r.POST:
    form = FormSuratMasuk(r.POST,r.FILES)
    id = r.POST['id']
    context={
    'judul':'Halaman Surat Masuk',
    'menu':'masuk',
    'form':form

    }
    surat_masuk = get_object_or_404(SuratMasuk, pk=id)
    if form.is_valid():
      surat_masuk.nomor = form.cleaned_data['nomor']
      surat_masuk.tgl_surat = form.cleaned_data['tgl_surat']
      surat_masuk.perihal = form.cleaned_data['perihal']
      surat_masuk.pengirim = form.cleaned_data['pengirim']
      surat_masuk.deskripsi = form.cleaned_data['deskripsi']
      surat_masuk.asal_instansi = form.cleaned_data['asal_instansi']
      surat_masuk.tgl_masuk = form.cleaned_data['tgl_masuk']
    

      surat_masuk.save(force_update=True)
      return redirect('surat:surat_masuk_list')
    return render(r, 'surat/surat_masuk_form_edit.html',context)

  surat_masuk = get_object_or_404(SuratMasuk, pk=id)
  form = FormSuratMasuk(initial={
          'nomor':surat_masuk.nomor,
          'tgl_surat':surat_masuk.tgl_surat,
          'perihal':surat_masuk.perihal,
          'pengirim':surat_masuk.pengirim,
          'deskripsi':surat_masuk.deskripsi,
          'asal_instansi':surat_masuk.asal_instansi,
          'tgl_masuk':surat_masuk.tgl_masuk,
        })
  context={
    'judul':'Halaman Surat Masuk',
    'menu':'masuk',
    'form':form,
    'id':surat_masuk.id

    }
  return render(r, 'surat/surat_masuk_form_edit.html',context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_masuk_form(request):
  form = FormSuratMasuk(request.POST,request.FILES)
  context={
    'judul':'Halaman Surat Masuk',
    'menu':'masuk',
    'form':form

    }
  if request.POST:
    if form.is_valid():
      form.save(commit=True)

      return redirect('surat:surat_masuk_list')

    return render(request, "surat/surat_masuk_form_new.html",context )

  return render(request, "surat/surat_masuk_form_new.html", context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_keluar_form(request):
  form = FormSuratKeluar(request.POST,request.FILES)
  context={
    'judul':'Halaman Form Surat Keluar',
    'menu':'keluar',
    'form':form

    }
  if request.POST:
    if form.is_valid():
      form.save(commit=True)

      return redirect('surat:surat_keluar_list')

    return render(request, "surat/surat_keluar_form_new.html",context)

  return render(request, "surat/surat_keluar_form_new.html", context)

# @login_required(login_url='login_page')
# @ijinkan_pengguna(yang_diizinkan=['administrator']) 
# def surat_keluar_list(request):
#   return render(request, "surat/surat_keluar_list.html", {
#     'data': SuratKeluar.objects.all().order_by('-id')
#   })

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_keluar_list(request):
  data= SuratKeluar.objects.all().order_by('-id')
  context={
    'judul':'Halaman List Surat Keluar',
    'menu':'keluar',
    'data':data

  }
  return render(request, "surat/surat_keluar_list.html",context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_keluar_delete(request, id):
  surat_keluar = get_object_or_404(SuratKeluar, pk=id)
  surat_keluar.delete()
  return redirect('surat:surat_keluar_list')

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def surat_keluar_edit(r, id):
  if r.POST:
    form = FormSuratKeluar(r.POST, r.FILES)
    id = r.POST['id']
    surat_keluar = get_object_or_404(SuratKeluar, pk=id)
    if form.is_valid():
      surat_keluar.nomor = form.cleaned_data['nomor']
      surat_keluar.tgl_surat = form.cleaned_data['tgl_surat']
      surat_keluar.perihal = form.cleaned_data['perihal']
      surat_keluar.pengirim = form.cleaned_data['pengirim']
      surat_keluar.deskripsi = form.cleaned_data['deskripsi']
      surat_keluar.asal_instansi = form.cleaned_data['asal_instansi']
      surat_keluar.tgl_masuk = form.cleaned_data['tgl_masuk']

      surat_keluar.save(force_update=True)
      return redirect('surat:surat_keluar_list')
    context={
    'judul':'Halaman List Surat Keluar',
    'menu':'keluar',
    'form':form,
    'id':id

  }
    return render(r, 'surat/surat_keluar_form_edit.html',context)

  surat_keluar = get_object_or_404(SuratKeluar, pk=id)
  form = FormSuratMasuk(initial={
          'nomor':surat_keluar.nomor,
          'tgl_surat':surat_keluar.tgl_surat,
          'perihal':surat_keluar.perihal,
          'pengirim':surat_keluar.pengirim,
          'deskripsi':surat_keluar.deskripsi,
          'tujuan_instansi':surat_keluar.tujuan_instansi,
          'tgl_keluar':surat_keluar.tgl_keluar,
        })
  context={
    'judul':'Halaman List Surat Keluar',
    'menu':'keluar',
    'form':form,
    'id':surat_keluar.id

  }
  return render(r, 'surat/surat_keluar_form_edit.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
# def instansi_list(request):
#   return render(request, "instansi/list.html", {
#     'data': Instansi.objects.all().order_by('-id')
#   })
def instansi_list(request):
  data=  Instansi.objects.all().order_by('-id')
  context={
     'judul':'Halaman List Surat Masuk',
    'menu':'instansi',
    'data':data

  }
  return render(request, "instansi/list.html",context)

@login_required
def instansi_delete(request, id):
  instansi = get_object_or_404(Instansi, pk=id)
  instansi.delete()
  return redirect('surat:instansi_list')

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def instansi_edit(r, id):
  if r.POST:
    form = FormInstansi(r.POST or None)
    id = r.POST['id']
    instansi = get_object_or_404(Instansi, pk=id)
    if form.is_valid():
      instansi.nama_instansi = form.cleaned_data['nama_instansi']
      instansi.kategori = form.cleaned_data['kategori']
      instansi.telepon = form.cleaned_data['telepon']
      instansi.kode_pos = form.cleaned_data['kode_pos']
      instansi.alamat = form.cleaned_data['alamat']

      instansi.save(force_update=True)
      return redirect('surat:instansi_list')
  
  instansi = get_object_or_404(Instansi, pk=id)
  form = FormInstansi(initial={
          'nama_instansi':instansi.nama_instansi,
          'kategori':instansi.kategori,
          'telepon':instansi.telepon,
          'kode_pos':instansi.kode_pos,
          'alamat':instansi.alamat,
        })
  context={
    'judul':'Halaman List Surat Masuk',
    'menu':'instansi',
    'form':form,
    'id':instansi.id

  }
  return render(r, 'instansi/form_edit.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def instansi_new(r):
  form = FormInstansi(r.POST or None)

  if r.POST:
    if form.is_valid():
      form.save(commit=True)
      return redirect('surat:instansi_list')
  context={
    'judul':'Halaman List Surat Masuk',
    'menu':'instansi',
    'form':form,

  }
    
  return render(r, 'instansi/form_new.html',context)
def logoutPage(request):
  logout(request)
  return redirect('login_page')



@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def struktural_admin(request):
    struktural = Struktural.objects.all()
    context = {
        'data': struktural,
        'judul': 'Halaman Struktural ',
        'menu': 'struktural',
    }
    return render(request, 'struktural/struktural_list.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formstruktural_admin(request):
    form = StrukturalForm()
    formuser = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = True
        user.save()

        akses = Group.objects.get(name='struktur')
        user.groups.add(akses)

        formsimpan = StrukturalForm(request.POST)
        if formsimpan.is_valid():
            data = formsimpan.save()
            data.user = user
            data.save()
            return redirect('surat:struktural_admin')
    context = {
        'judul': 'Halaman Form Struktural',
        'menu': 'struktural',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'struktural/struktural_new.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editstruktural_admin(request, pk):
    struktural = Struktural.objects.get(id=pk)
    user = User.objects.get(id=struktural.user.id)
    form = StrukturalForm(instance=struktural)
    formuser = UserForm(instance=user)
    if request.method == 'POST':
        formsimpan = StrukturalForm(request.POST,request.FILES, instance=struktural)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('surat:struktural_admin')
    context = {
       'judul': 'Halaman Form Edit Struktural',
        'menu': 'struktural',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'struktural/struktural_new.html', context)

@login_required
def struktutal_delete(request, id):
  struktural = get_object_or_404(Struktural, pk=id)
  struktural.delete()
  return redirect('surat:struktural_admin')

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def laporan_admin(request):
    struktural = Struktural.objects.all()
    context = {
        'data': struktural,
        'judul': 'Halaman Struktural ',
        'menu': 'laporan',
    }
    return render(request, 'laporan/laporan_list.html', context)

def data_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="suratmasuk.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Surat Masuk')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nomor', 'Tgl Surat','Perihal','Pengirim','Deskripsi','Asal Instansi','Tanggal Masuk' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = SuratMasuk.objects.all().values_list('nomor', 'tgl_surat','perihal','pengirim','deskripsi','asal_instansi__nama_instansi','tgl_masuk')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def data_export_keluar(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="suratkeluar.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Surat Keluar')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nomor', 'Tgl Surat','Perihal','Pengirim','Deskripsi','Tujuan Instansi','Tanggal Keluar' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = SuratKeluar.objects.all().values_list('nomor', 'tgl_surat','perihal','pengirim','deskripsi','tujuan_instansi__nama_instansi','tgl_keluar')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def data_export_detail_keluar(request):
    tgl_mulai_keluar = request.POST['tgl_mulai_keluar'] 
    tgl_akhir_keluar = request.POST['tgl_akhir_keluar']
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="suratkeluardetail.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Surat Keluar')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nomor', 'Tgl Surat','Perihal','Pengirim','Deskripsi','Tujuan Instansi','Tanggal Keluar' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = SuratKeluar.objects.all().values_list('nomor', 'tgl_surat','perihal','pengirim','deskripsi','tujuan_instansi__nama_instansi','tgl_keluar').filter(created__range=(tgl_mulai_keluar, tgl_akhir_keluar))
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
  
def data_export_detail(request):
    tgl_mulai_masuk = request.POST['tgl_mulai_masuk'] 
    tgl_akhir_masuk = request.POST['tgl_akhir_masuk']

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="suratmasukdetail.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Surat Masuk')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nomor', 'Tgl Surat','Perihal','Pengirim','Deskripsi','Asal Instansi','Tanggal Masuk','Tembusan' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = SuratMasuk.objects.all().values_list('nomor', 'tgl_surat','perihal','pengirim','deskripsi','asal_instansi__nama_instansi','tgl_masuk','disposisi__tujuan_disposisi').filter(created__range=(tgl_mulai_masuk, tgl_akhir_masuk))
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['struktur']) 
def struktur_beranda(request):
  jmlSuratMasuk = SuratMasuk.objects.all().count()
  jmlSuratKeluar = SuratKeluar.objects.all().count()
  jmlInstansi = Instansi.objects.all().count()
  jmlStruktural = Struktural.objects.all().count()
  context={
    'judul':'Halaman Beranda Struktural',
    'menu':'struktur',
    'jmlSuratMasuk':jmlSuratMasuk,
        'jmlSuratKeluar':jmlSuratKeluar,
        'jmlInstansi':jmlInstansi,
        'jmlStruktural':jmlStruktural,

  }
  return render(request, 'struktur/home.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['struktur']) 
def disposisi_beranda(request):

  id_struktural = request.user.struktural.id
  struktural = Struktural.objects.get(id=id_struktural)
  data= Disposisi.objects.all().filter(tujuan_disposisi__id=struktural.id).order_by('-id')
  context={
    'judul':'Halaman Disposisi',
    'menu':'disposisi',
    'data':data
    

  }
  return render(request, 'struktur/disposisi.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def disposisi_admin(request):

  
  data= Disposisi.objects.all().order_by('-id')
  context={
    'judul':'Halaman Disposisi',
    'menu':'disposisiadmin',
    'data':data
  }
  return render(request, 'surat/disposisi_admin.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def disposisi_admin_keluar(request):

  
  data= Disposisi_keluar.objects.all().order_by('-id')
  context={
    'judul':'Halaman Disposisi',
    'menu':'disposisikeluaradmin',
    'data':data
  }
  return render(request, 'surat/disposisi_admin_keluar.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def data_disposisi(request, id):
      idsurat = SuratMasuk.objects.get(id=id)
      
      cekdiposis = Disposisi.objects.filter(suratmasuk__id=idsurat.id).all().count()
      if cekdiposis > 0:
          id = Disposisi.objects.get(suratmasuk__id=idsurat.id)
          form =FormDiposisi(instance= id)
          if request.method == 'POST':
                formsimpan = FormDiposisi(request.POST,instance= id)
                if formsimpan.is_valid():
                  formsimpan.save()
                  return redirect('surat:surat_masuk_list')
      else:
          form =FormDiposisi()
          if request.method == 'POST':
                formsimpan = FormDiposisi(request.POST)
                if formsimpan.is_valid():
                  simpan = formsimpan.save()
                  simpan.suratmasuk = idsurat
                  simpan.save()
                  return redirect('surat:surat_masuk_list')
      context={
        'judul':'Halaman Disposisi',
        'menu':'masuk',
        'form':form
       
        

      }
      return render(request, 'surat/disposisi.html',context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def data_disposisi_keluar(request, id):
      idsurat = SuratKeluar.objects.get(id=id)
      
      cekdiposis = Disposisi_keluar.objects.filter(suratkeluar__id=idsurat.id).all().count()
      if cekdiposis > 0:
          id = Disposisi_keluar.objects.get(suratkeluar__id=idsurat.id)
          form =FormDiposisiKeluar(instance= id)
          if request.method == 'POST':
                formsimpan = FormDiposisiKeluar(request.POST,instance= id)
                if formsimpan.is_valid():
                      formsimpan.save()
                      return redirect('surat:surat_keluar_list')
      else:
          form =FormDiposisiKeluar()
          if request.method == 'POST':
                formsimpan = FormDiposisiKeluar(request.POST)
                if formsimpan.is_valid():
                      simpan = formsimpan.save()
                      simpan.suratkeluar = idsurat
                      simpan.save()
                      return redirect('surat:surat_keluar_list')
      context={
        'judul':'Halaman Disposisi Keluar',
        'menu':'keluar',
        'form':form
      }
      return render(request, 'surat/disposisi_keluar.html',context)

@login_required(login_url='login_page')
def cetak_disposisi(request, id):
      idsurat = SuratMasuk.objects.get(id=id)
      disposisi =Disposisi.objects.filter(suratmasuk__id=idsurat.id).all()
      
      context={
        'judul':'Halaman Disposisi',
        'menu':'disposisi',
        'data':idsurat,
        'disposisi':disposisi,
       
        

      }
      return render(request, 'surat/cetak.html',context)
    
@login_required(login_url='login_page')
def cetak_disposisi_keluar(request, id):
      idsurat = SuratKeluar.objects.get(id=id)
      disposisi =Disposisi_keluar.objects.filter(suratkeluar__id=idsurat.id).all()
      
      context={
        'judul':'Halaman Disposisi',
        'menu':'disposisi',
        'data':idsurat,
        'disposisi':disposisi,
       
        

      }
      return render(request, 'surat/cetak_keluar.html',context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['struktur']) 
def surat_masuk_list_struktural(request):
  data= SuratMasuk.objects.all().order_by('-id')
  context={
     'judul':'Halaman List Surat Masuk',
    'menu':'masuk',
    'data':data

  }
  return render(request, "struktur/surat_masuk_list_struktural.html",context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['struktur']) 
def surat_keluar_list_struktural(request):
  data= SuratKeluar.objects.all().order_by('-id')
  context={
     'judul':'Halaman List Surat Keluar',
    'menu':'keluar',
    'data':data

  }
  return render(request, "struktur/surat_keluar_list_struktural.html",context)
  
    
    
