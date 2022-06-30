from esg_api.models import Customer, Corp
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from . import corp_created


# Creating user and Customer in their own app
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # this function will be called when user model had been saved
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:  # returns boolean
        Customer.objects.create(user=kwargs['instance'])


@receiver(corp_created, sender=Corp)
def scraping_corps_esg_scores(sender, **kwargs):
    pass
