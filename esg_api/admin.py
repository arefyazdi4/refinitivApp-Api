from django.contrib import admin
from . import models


@admin.register(models.Corp)
class CorpAdmin(admin.ModelAdmin):
    list_display = ['title', 'industry_type']
    list_per_page = 20


@admin.register(models.ESGScore)
class ESGScoreAdmin(admin.ModelAdmin):
    list_display = ['corp', 'esg_score', 'rank', 'reliability']
    list_editable = ['rank']
    list_per_page = 20

    @admin.display(ordering='esg_score')
    def reliability(self, esgscore):
        score = esgscore.esg_score
        if score < 25:
            return 'poor performance'
        elif score < 50:
            return 'satisfactory performance'
        elif score < 75:
            return 'good performance'
        elif score <= 100:
            return 'excellent performance'
