from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def senf_pdf(receiver: str, pdf_file):
    email = EmailMessage(
        subject="Requested CV",
        body="Find attached the requested CV",
        from_email=None,
        to=[receiver],
    )
    # Attach the PDF
    email.attach('CV.pdf', pdf_file, 'application/pdf')

    email.send()