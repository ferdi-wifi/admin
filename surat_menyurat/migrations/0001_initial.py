# Generated by Django 3.1.7 on 2022-07-26 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instansi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_instansi', models.CharField(max_length=255)),
                ('kategori', models.CharField(choices=[('swasta', 'Swasta'), ('pemerintah', 'Pemerintah')], max_length=255)),
                ('telepon', models.CharField(blank=True, max_length=255, null=True)),
                ('kode_pos', models.CharField(blank=True, max_length=255, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Nama Instansi',
            },
        ),
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.CharField(max_length=255)),
                ('tgl_surat', models.CharField(help_text='Tanggal di dalam isi surat', max_length=255, verbose_name='Tanggal surat')),
                ('perihal', models.CharField(max_length=255)),
                ('pengirim', models.CharField(blank=True, help_text='Orang atau jasa yang mengantar surat', max_length=255, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Surat',
            },
        ),
        migrations.CreateModel(
            name='Struktural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('jabatan', models.CharField(max_length=200)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data Struktural',
            },
        ),
        migrations.CreateModel(
            name='Disposisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batas_waktu', models.CharField(help_text='Tanggal keluar surat dari kantor', max_length=255, verbose_name='Batas Waktu')),
                ('isi_disposisi', models.TextField(blank=True, null=True)),
                ('catatan', models.CharField(max_length=255)),
                ('sifat_disposisi', models.CharField(choices=[('Biasa', 'Biasa'), ('Segera', 'Segera'), ('Penting', 'Penting'), ('Rahasia', 'Rahasia')], default='', max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('surat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.surat')),
                ('tujuan_disposisi', models.ForeignKey(help_text='Jika tujuan disposisi tidak ada, silahkan ke menu disposisi', on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.struktural')),
            ],
            options={
                'verbose_name_plural': 'Disposisi',
            },
        ),
        migrations.CreateModel(
            name='SuratMasuk',
            fields=[
                ('surat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='surat_menyurat.surat')),
                ('tgl_masuk', models.CharField(help_text='Tanggal masuk surat ke kantor', max_length=255, verbose_name='Tanggal masuk')),
                ('file_surat_masuk', models.FileField(blank=True, max_length=300, null=True, upload_to='arsip/file_surat_masuk')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('asal_instansi', models.ForeignKey(help_text='Jika asal instansi tidak ada, silahkan ke menu instansi', on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.instansi')),
            ],
            options={
                'verbose_name_plural': 'Surat Masuk',
            },
            bases=('surat_menyurat.surat',),
        ),
        migrations.CreateModel(
            name='SuratKeluar',
            fields=[
                ('surat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='surat_menyurat.surat')),
                ('tgl_keluar', models.CharField(help_text='Tanggal keluar surat dari kantor', max_length=255, verbose_name='Tanggal keluar')),
                ('file_surat_keluar', models.FileField(blank=True, max_length=300, null=True, upload_to='arsip/file_surat_keluar')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tujuan_instansi', models.ForeignKey(help_text='Jika tujuan instansi tidak ada, silahkan ke menu instansi', on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.instansi')),
            ],
            options={
                'verbose_name_plural': 'Surat Keluar',
            },
            bases=('surat_menyurat.surat',),
        ),
    ]
