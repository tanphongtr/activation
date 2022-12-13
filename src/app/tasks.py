from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(name='Task Example')
def task_example(params):
    pass

