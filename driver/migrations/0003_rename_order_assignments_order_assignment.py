# Generated by Django 5.0.4 on 2024-05-01 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_vehicle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_assignments',
            new_name='Order_assignment',
        ),
    ]
