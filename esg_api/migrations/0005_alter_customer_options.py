# Generated by Django 3.2.8 on 2022-06-15 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esg_api', '0004_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
