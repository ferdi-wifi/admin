from django.urls import path, include
from . import views

app_name ='surat_menyurat'

urlpatterns = [
  path('instansi/', views.instansi_list, name='instansi_list'),
  path('instansiform/', views.instansi_new, name='instansi_form'),
  path('instansidelete/<int:id>', views.instansi_delete, name='instansi_delete'),
  path('instansiedit/<int:id>', views.instansi_edit, name='instansi_edit'),
   path('logout', views.logoutPage, name='logout'),
  path('suratmasuk/', views.surat_masuk_list, name='surat_masuk_list'),
  path('suratmasukform/', views.surat_masuk_form, name='surat_masuk_form'),
  path('suratmasukdelete/<int:id>', views.surat_masuk_delete, name='surat_masuk_delete'),
  path('suratmasukedit/<int:id>', views.surat_masuk_edit, name='surat_masuk_edit'),
  path('data-disposisi/<int:id>', views.data_disposisi, name='data_disposisi'),
  path('cetak-disposisi/<int:id>', views.cetak_disposisi, name='cetak_disposisi'),

  path('suratkeluar/', views.surat_keluar_list, name='surat_keluar_list'),
  path('suratkeluarform/', views.surat_keluar_form, name='surat_keluar_form'),
  path('suratkeluardelete/<int:id>', views.surat_keluar_delete, name='surat_keluar_delete'),
  path('suratkeluaredit/<int:id>', views.surat_keluar_edit, name='surat_keluar_edit'),
  path('data-disposisi-keluar/<int:id>', views.data_disposisi_keluar, name='data_disposisi_keluar'),
  path('cetak-disposisi-keluar/<int:id>', views.cetak_disposisi_keluar, name='cetak_disposisi_keluar'),


  path('struktural-admin/', views.struktural_admin, name='struktural_admin'),
  path('form-struktural/', views.formstruktural_admin, name='formstruktural_admin'),
  path('edit-struktural/<str:pk>', views.editstruktural_admin, name='editstruktural_admin'),
  path('delete-struktural/<str:id>', views.struktutal_delete, name='struktutal_delete'),

  path('laporan/', views.laporan_admin, name='laporan_admin'),
  path('data-export/', views.data_export, name='data_export'),
  path('data-export-keluar/', views.data_export_keluar, name='data_export_keluar'),

  path('data-export-detail/', views.data_export_detail, name='data_export_detail'),
  path('data-export-detail-keluar/', views.data_export_detail_keluar, name='data_export_detail_keluar'),

  path('struktur/', views.struktur_beranda, name='struktur_beranda'),
  path('disposis/', views.disposisi_beranda, name='disposisi_beranda'),


  path('disposis-admin/', views.disposisi_admin, name='disposisi_admin'),
  path('disposis-admin-keluar/', views.disposisi_admin_keluar, name='disposisi_admin_keluar'),


   path('suratmasuk-struktural/', views.surat_masuk_list_struktural, name='surat_masuk_list_struktural'),
   path('suratkeluar-struktural/', views.surat_keluar_list_struktural, name='surat_keluar_list_struktural'),
]
