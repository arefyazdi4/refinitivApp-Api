from django.core.validators import MinValueValidator
from django.db import models


class Corp(models.Model):
    title = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255, unique=True)
    industry_type = models.TextField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class ESGScore(models.Model):
    rank = models.IntegerField()
    total_industries = models.IntegerField(validators=[MinValueValidator(0)])
    esg_score = models.IntegerField()
    environment_pillar = models.IntegerField()
    governance_pillar = models.IntegerField()
    social_pillar = models.IntegerField()
    corp = models.OneToOneField(Corp, on_delete=models.CASCADE, primary_key=True)

    objects = models.Manager()
