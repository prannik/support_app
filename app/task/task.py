from app.task.utils import send_email
from config.celery import app


@app.task
def send_update_status(title_problem, new_status, email_author):
    """ Sending email about status change """

    title = f'New status in the "{title_problem}"'
    body = f'In the problem "{title_problem}" the status changed to "{new_status}"'
    send_email(title, body, email_author)
