# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-08 01:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('GERBLE', 'Gerble'), ('HAMSTER', 'Hamster')], max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=75)),
                ('image', models.FileField(upload_to='uploads/')),
                ('description', models.FileField(default='Description', upload_to=b'')),
                ('adoption_ready', models.BooleanField(default=False)),
                ('foster_ready', models.BooleanField(default=False)),
                ('viewable', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image', models.FileField(upload_to='uploads/')),
                ('description', models.FileField(default='Description', upload_to=b'')),
                ('data', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FosterParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('zipcode', models.CharField(max_length=5)),
                ('street_address', models.CharField(max_length=45)),
                ('email_address', models.CharField(max_length=45)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '123-456-7890'.", regex='^\\d{3}-\\d{3}-{4}$')])),
                ('animal_type_preference', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('image', models.FileField(upload_to='uploads/')),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='fosterParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animalRescue_app.FosterParent'),
        ),
    ]
