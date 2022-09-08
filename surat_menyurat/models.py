from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Struktural(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    jabatan = models.CharField(max_length=200, blank=False,)
    alamat = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.jabatan
    class Meta:
        verbose_name_plural ="Data Struktural"

class Instansi(models.Model):
      KATEGORI_INSTANSI = (
    ('swasta', 'Swasta'),
    ('pemerintah', 'Pemerintah'),
    )

      nama_instansi = models.CharField(max_length=255, blank=False, null=False)
      kategori      = models.CharField(max_length=255, choices=KATEGORI_INSTANSI)
      telepon       = models.CharField(max_length=255, blank=True, null=True)
      kode_pos      = models.CharField(max_length=255, blank=True, null=True)
      alamat        = models.TextField(blank=True, null=True)
      created       = models.DateTimeField(auto_now=False, auto_now_add=True)
      updated       = models.DateTimeField(auto_now=True, auto_now_add=False)

      def __str__(self):
            return self.nama_instansi
      class Meta:
            verbose_name_plural ="Nama Instansi"

class Surat(models.Model):
      nomor         = models.CharField(max_length=255, blank=False, null=False)
      tgl_surat     = models.CharField(
                      _("Tanggal surat"),
                      help_text=_('Tanggal di dalam isi surat'),
                      max_length=255, blank=False, null=False)
      perihal       = models.CharField(max_length=255, blank=False, null=False)
      pengirim      = models.CharField(
                      help_text=_('Orang atau jasa yang mengantar surat'),
                      max_length=255, blank=True, null=True)
      deskripsi     = models.TextField(blank=True, null=True)

      def __str__(self):
            return self.nomor
      class Meta:
            verbose_name_plural ="Surat"

class SuratMasuk(Surat):
      asal_instansi = models.ForeignKey(
                      Instansi,
                      help_text=_('Jika asal instansi tidak ada, silahkan ke menu instansi'),
                      on_delete=models.CASCADE)
      tgl_masuk     = models.CharField(
                      _("Tanggal masuk"),
                      help_text=_('Tanggal masuk surat ke kantor'),
                      max_length=255, blank=False, null=False)
      
      file_surat_masuk = models.FileField(upload_to='arsip/file_surat_masuk',blank=True, null=True,max_length=300)
      created       = models.DateTimeField(auto_now=False, auto_now_add=True)
      updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
      
      def __str__(self):
            return self.tgl_masuk
      class Meta:
            verbose_name_plural ="Surat Masuk"

class SuratKeluar(Surat):
      tujuan_instansi   = models.ForeignKey(
                          Instansi,
                          help_text=_('Jika tujuan instansi tidak ada, silahkan ke menu instansi'),
                          on_delete=models.CASCADE)
      tgl_keluar        = models.CharField(
                          _("Tanggal keluar"),
                          help_text=_('Tanggal keluar surat dari kantor'),
                          max_length=255, blank=False, null=False)
      file_surat_keluar = models.FileField(upload_to='arsip/file_surat_keluar',blank=True, null=True,max_length=300)
      created           = models.DateTimeField(auto_now=False, auto_now_add=True)
      updated           = models.DateTimeField(auto_now=True, auto_now_add=False)

      def __str__(self):
            return self.nomor
      class Meta:
            verbose_name_plural ="Surat Keluar"

class Disposisi(models.Model):
      SIFAT_DISPOSISI = (
      ('Biasa', 'Biasa'),
      ('Segera', 'Segera'),
      ('Penting', 'Penting'),
      ('Rahasia', 'Rahasia'),
      )
      tujuan_disposisi   = models.ForeignKey(Struktural,on_delete=models.CASCADE,blank=True, null=True)
      suratmasuk             = models.ForeignKey(SuratMasuk,on_delete=models.CASCADE,default="",null=True)
      batas_waktu        = models.CharField(max_length=255, blank=False, null=False)
      isi_disposisi     = models.TextField(blank=True, null=True)
      catatan           = models.CharField(max_length=255, blank=False, null=False)
      sifat_disposisi   = models.CharField(max_length=255, blank=False, default="", null=False,choices=SIFAT_DISPOSISI)
      updated           = models.DateTimeField(auto_now=True, auto_now_add=False)

      def __str__(self):
            return self.sifat_disposisi
      class Meta:
            verbose_name_plural ="Disposisi Masuk"

class Disposisi_keluar(models.Model):
      SIFAT_DISPOSISI = (
      ('Biasa', 'Biasa'),
      ('Segera', 'Segera'),
      ('Penting', 'Penting'),
      ('Rahasia', 'Rahasia'),
      )
      tujuan_disposisi   = models.ForeignKey(Struktural,on_delete=models.CASCADE,blank=True, null=True)
      suratkeluar           = models.ForeignKey(SuratKeluar,on_delete=models.CASCADE,default="",null=True)
      batas_waktu        = models.CharField(max_length=255, blank=False, null=False)
      isi_disposisi     = models.TextField(blank=True, null=True)
      catatan           = models.CharField(max_length=255, blank=False, null=False)
      sifat_disposisi   = models.CharField(max_length=255, blank=False, default="", null=False,choices=SIFAT_DISPOSISI)
      updated           = models.DateTimeField(auto_now=True, auto_now_add=False)

      def __str__(self):
            return self.sifat_disposisi
      class Meta:
            verbose_name_plural ="Disposisi Keluar"
