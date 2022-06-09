from django.contrib import admin, messages
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


class ReliabilityFilter(admin.SimpleListFilter):
    title = 'Reliability'
    parameter_name = 'reliability'

    def lookups(self, request, model_admin):
        return [
            ('<25', 'poor'),
            ('<50', 'satisfactory'),
            ('<75', 'good'),
            ('<100', 'excellent')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<25':
            return queryset.filter(rank__lt=25)
        elif self.value() == '<50':
            return queryset.filter(rank__lt=50)
        elif self.value() == '<75':
            return queryset.filter(rank__lt=75)
        elif self.value() == '<100':
            return queryset.filter(rank__lte=100)


@admin.register(models.Corp)
class CorpAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'ticker': ['title']
    }
    list_display = ['title', 'ticker', 'esgscore_rank', 'industry_type']
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
    autocomplete_fields = ['corp']
    actions = ['reset_esg_scores']
    list_display = ['corp', 'esg_score', 'rank', 'reliability',
                    'environment_pillar', 'governance_pillar', 'social_pillar']
    list_editable = ['rank']
    list_filter = [ReliabilityFilter]
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

    @admin.action(description='Reset ESG Scores')
    def reset_esg_scores(self, request, queryset):
        updated_scores = queryset.update(esg_score=0)
        self.message_user(
            request,
            f'{updated_scores} ESG Scores were successfully updated',
            messages.WARNING
        )
