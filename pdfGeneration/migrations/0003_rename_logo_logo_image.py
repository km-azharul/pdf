# Generated by Django 3.2.3 on 2021-06-20 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfGeneration', '0002_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logo',
            old_name='logo',
            new_name='image',
        ),
    ]