# Generated by Django 3.2.8 on 2022-06-06 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ticker', models.CharField(max_length=255, unique=True)),
                ('industry_type', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
                ('total_industries', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('esg_score', models.IntegerField()),
                ('environment_pillar', models.IntegerField()),
                ('governance_pillar', models.IntegerField()),
                ('social_pillar', models.IntegerField()),
            ],
        ),
    ]
