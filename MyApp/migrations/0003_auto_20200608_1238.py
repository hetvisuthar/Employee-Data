# Generated by Django 2.2 on 2020-06-08 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20200607_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='emplyoee_name',
            new_name='employee_name',
        ),
    ]
