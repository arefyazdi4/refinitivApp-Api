from rest_framework import serializers
from .models import Corp, ESGScore


class ESGScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESGScore
        fields = ['corp', 'rank', 'esg_score',
                  'environment_pillar', 'governance_pillar', 'social_pillar']

    corp = serializers.StringRelatedField()
    rank = serializers.SerializerMethodField(method_name='rank_out_of')

    def rank_out_of(self, esgscore: ESGScore):
        return f'{esgscore.rank}/{esgscore.total_industries}'


class CorpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corp
        fields = ['id', 'title', 'ticker', 'industry_type', 'esgscore']

    esgscore = ESGScoreSerializer()
