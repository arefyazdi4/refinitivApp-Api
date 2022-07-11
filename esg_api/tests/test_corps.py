from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCorp:
    def test_if_use_anonymous_return_401(self):
        client = APIClient()
        response = client.post(path='/api/corps/', data={'title': 'test_corp_title'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
