from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """
    A view to return the contact form page
    """
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['kiran.satyarthy@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            messages.success(request, (
                "Thank you for contacting Superchef."
                "We will respond to you as soon as possible."
            ))
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
