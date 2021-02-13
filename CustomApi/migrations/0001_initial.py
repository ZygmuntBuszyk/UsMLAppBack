# Generated by Django 3.1.5 on 2021-02-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userLoanData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=18)),
                ('lastname', models.CharField(max_length=18)),
                ('dependants', models.IntegerField(default=0)),
                ('applicantincome', models.IntegerField(default=0)),
                ('coapplicatincome', models.IntegerField(default=0)),
                ('loanamt', models.IntegerField(default=0)),
                ('loanterm', models.IntegerField(default=0)),
                ('credithistory', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=18)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=18)),
                ('graduatededucation', models.CharField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')], max_length=18)),
                ('selfemployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=18)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.UUIDField(blank=True, default=None, null=True, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('approved', models.BooleanField(default=None, null=True)),
                ('loanDataId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomApi.userloandata')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
