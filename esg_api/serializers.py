from rest_framework import serializers
from .models import Corp, ESGScore, Customer
from .signals import corp_created


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

    def save(self, **kwargs):
        corp_created.send_robust(self.__class__)


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']
