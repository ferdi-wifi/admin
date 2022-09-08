from django.contrib import admin
from .models import Instansi, SuratMasuk, SuratKeluar,Disposisi,Struktural

admin.site.register(Instansi)
admin.site.register(SuratMasuk)
admin.site.register(SuratKeluar)
admin.site.register(Disposisi)
admin.site.register(Struktural)