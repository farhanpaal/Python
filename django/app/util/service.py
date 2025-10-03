from django.core.mail import send_mail
from django.conf import settings

def SendMail(subject, message, recipient):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient
        )
        return{
            'success': True
        }
    except:
        return{
            'success': False,
            'message': 'Failed to send email'
        }