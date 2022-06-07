from rest_framework import serializers
from .models import Corp, ESGScore


class CorpSerializer(serializers.ModelSerializer):  # change base class to 'ModelSerializer'
    class Meta:
        model = Corp
        fields = ['id', 'title', 'ticker', 'industry_type', 'esg_score']

    esg_score = serializers.HyperlinkedRelatedField(
        queryset=ESGScore.object.all(),
        view_name='esg-score'
    )


class ESGScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESGScore
        fields = ['corp', 'rank', 'esg_score',
                  'environment_pillar', 'governance_pillar', 'social_pillar']

    corp = CorpSerializer()
    rank = serializers.SerializerMethodField(method_name='rank_out_of')

    def rank_out_of(self, esgscore: ESGScore):
        return f'{esgscore.rank}/{esgscore.total_industries}'
