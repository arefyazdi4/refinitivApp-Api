from esg_api.models import Customer, Corp
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from esg_api.tasks import scraping_esg_scores


# Creating user and Customer in their own app
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # this function will be called when user model had been saved
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:  # returns boolean
        Customer.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=Corp)
def scraping_corps_esg_scores(sender, **kwargs):
    print('process started')
    scraping_esg_scores.delay()