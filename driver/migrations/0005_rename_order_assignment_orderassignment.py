# Generated by Django 5.0.4 on 2024-05-02 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_alter_order_assignment_driver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_assignment',
            new_name='OrderAssignment',
        ),
    ]
