from django.core.mail import send_mail  #we send mail using this function
from django.conf import settings  #we used so that we can use varibles from settings.py
from django.template.loader import render_to_string

def SendPlainMail(subject, message, recipient):
    try: 
        # this is in the form if tupple
        send_mail(

            subject=subject,
            message=message,
            recipient_list=recipient,
            from_email=settings.EMAIL_HOST_USER,
        )
        return {
            'success': True
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }
    

def SendHtmlMail(subject, template,data, recipient):
    try: 
        html= render_to_string(template,data)

        # this is in the form if tupple
        send_mail(
            subject=subject,
            message=None, #this is used to send plain message
            html_message=html,
            recipient_list=recipient,
            from_email=settings.EMAIL_HOST_USER,
        )
        return {
            'success': True
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }
    
# service.py