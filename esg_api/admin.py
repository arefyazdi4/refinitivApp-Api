from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Corp)
class CorpAdmin(admin.ModelAdmin):
    list_display = ['title', 'industry_type', 'esgscore_rank']
    list_select_related = ['esgscore']
    list_per_page = 20
    ordering = ['title']
    search_fields = ['title', 'industry_type__istartswith']

    @admin.display(ordering='rank')
    def esgscore_rank(self, corp):
        url = (
                reverse('admin:esg_api_esgscore_changelist')
                + '?'
                + urlencode({'corp__id': str(corp.id)})
        )
        return format_html(f'<a herf="{url}">{corp.esgscore.rank}</a>')


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
