# Generated by Django 3.1.5 on 2021-01-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomApi', '0003_account_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='loanData',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomApi.userloandata'),
        ),
    ]