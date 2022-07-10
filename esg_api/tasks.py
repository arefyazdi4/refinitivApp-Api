from celery import shared_task


@shared_task
def scraping_esg_scores():
    print('Crawling throw web')
