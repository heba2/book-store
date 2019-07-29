from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm





def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['hebasalem623@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse("<h2 style='color:green;margin:20px;'>Your Message Sent Successfully ...</2>")
    return render(request, "contact/email.html", {'form': form})



