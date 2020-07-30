from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
import mimetypes
# Create your views here.
def index(request):
    return render(request, "fagan_port/index.html",{
        "active": 1
    })

def contact(request):
    return render(request, "fagan_port/contact.html",{
        "active": 3
    })

def blog(request):
    return render(request, "fagan_port/blog.html",{
        "active": 2
    })



def sendmail(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        subject_ = request.POST["subject"]
        text = request.POST["text"]
        print(fullname,email,subject_,text)
        subject, from_email, to = subject_, 'enough.good@mail.ru', email
        text_content = text
        html_content = '<h4>Dear '+fullname+',</h4>'+'<p>Thanks for your message</p>'+'<p>Your message:</p>'+'<p>'+text+'</p>'+'<p>I will come back you as much as possible!</p>'+'<hr>'+'<p>Kindly regards,</p>'+'<p>Fagan Rasulov</p>'+'<p>Tel:    (+994 70) 556 6041</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, "fagan_port/contact.html", {
            "message": "Your mail was sent successfully",
            "message_type": True,
            "active": 3,
        })
    return render(request, "fagan_port/contact.html", {
        "message": "Your mail was not sent!",
        "message_type": False,
        "active": 3,
    })
