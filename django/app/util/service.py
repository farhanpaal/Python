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
        return {
            'success': True
        }
    except Exception as e:
        print("Email error:", e)  # Add this line to see the error in your console
        return {
            'success': False,
            'message': f'Failed to send email: {e}'
        }