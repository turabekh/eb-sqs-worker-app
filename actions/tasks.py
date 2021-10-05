from .models import Action 
from webapp.logs import log_error, log_info
from django.core.mail import send_mail


def create_action(action):
    try:
        new_action = Action.objects.create(**action)
        log_info(f"Action Created. Action ID: {new_action.id}", "create_action")
    except:
        log_error(f"Action info: {action}", "create_action")



def send_single_email(message):
    try:
        send_mail(**message)
        log_info("Send Email task completed", "send_single_email")
    except Exception as e:
        log_error("Error in sending email", "send_single_email")