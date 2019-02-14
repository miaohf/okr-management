# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-14 22:06
from __future__ import unicode_literals

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
            name='KeyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type_data', models.CharField(choices=[(b'0', b'Positive'), (b'1', b'Negative'), (b'2', b'Binary')], default=b'0', max_length=1, verbose_name=b'Type')),
                ('obtained', models.FloatField()),
                ('expected', models.FloatField()),
                ('percentage', models.FloatField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name=b'publication date')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name=b'publication date')),
                ('end_date', models.DateField(verbose_name=b'end date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='keyresult',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okr.Objective'),
        ),
    ]
