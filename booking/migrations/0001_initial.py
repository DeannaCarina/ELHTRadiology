# Generated by Django 3.2 on 2022-01-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AngioAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('kidney_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='CtAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('exam_location', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('kidney_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='DexaAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('surgery_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='FluoroAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('exam_location', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('kidney_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='MammoAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('implants_status', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='MriAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('exam_location', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('kidney_status', models.CharField(max_length=100)),
                ('metal_status', models.CharField(max_length=100)),
                ('pacemaker_status', models.CharField(max_length=100)),
                ('eyes_status', models.CharField(max_length=100)),
                ('claustrophobia_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='NmAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('breastfeeding_status', models.CharField(max_length=100)),
                ('weight_status', models.CharField(max_length=100)),
                ('kidney_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='UsAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('exam_location', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='XrayAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('examination_type', models.CharField(max_length=100)),
                ('exam_location', models.CharField(max_length=100)),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
