# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Neigh', '0003_neighbourhood_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='business',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='title',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='business',
            name='User',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='description',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='email',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(default='name', max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Neigh.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Neigh.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='occupants_count',
            field=models.PositiveIntegerField(),
        ),
    ]