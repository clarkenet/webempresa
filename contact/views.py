from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                'La Caffetiera: Nuevo mensaje de contacto',
                f'De {name} <{email}>\n\nEscribió:\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ['pactoreal@msn.com'],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('Contact') + '?ok')
            except:
                return redirect(reverse('Contact') + '?fail')

    return render(request, 'contact/contact.html', {"page_name": "Contacto", "form": contact_form})
