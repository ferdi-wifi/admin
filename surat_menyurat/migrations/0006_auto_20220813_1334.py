# Generated by Django 3.1.7 on 2022-08-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surat_menyurat', '0005_auto_20220813_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='suratmasuk',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.suratmasuk'),
        ),
        migrations.AlterField(
            model_name='disposisi_keluar',
            name='suratkeluar',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='surat_menyurat.suratkeluar'),
        ),
    ]
