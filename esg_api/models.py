from django.core.validators import MinValueValidator
from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255, unique=True)
    industry_type = models.TextField(blank=True)
    rank = models.IntegerField()
    total_industries = models.IntegerField(validators=[MinValueValidator(0)])
    esg_score = models.IntegerField()
    environment_pillar = models.IntegerField()
    governance_pillar = models.IntegerField()
    social_pillar = models.IntegerField()
