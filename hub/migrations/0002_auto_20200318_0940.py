# Generated by Django 3.0.3 on 2020-03-18 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='address_type',
        ),
    ]