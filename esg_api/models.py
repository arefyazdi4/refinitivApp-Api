from django.core.validators import MinValueValidator
from django.db import models
from django.contrib import admin
from django.conf import settings


class Corp(models.Model):
    title = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255, unique=True)
    industry_type = models.TextField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class ESGScore(models.Model):
    rank = models.IntegerField()
    total_industries = models.IntegerField(validators=[MinValueValidator(0)])
    esg_score = models.IntegerField()
    environment_pillar = models.IntegerField()
    governance_pillar = models.IntegerField()
    social_pillar = models.IntegerField()
    corp = models.OneToOneField(Corp, on_delete=models.CASCADE, primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return self.corp

    class Meta:
        ordering = ['esg_score', 'rank']
        permissions = [
            ('rest_scores', 'Can reset all Scores')
        ]


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]
