# Generated by Django 3.2.8 on 2022-06-11 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esg_api', '0002_company_model_extend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corp',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='esgscore',
            options={'ordering': ['esg_score', 'rank'], 'permissions': [('rest_scores', 'Can reset all Scores')]},
        ),
    ]