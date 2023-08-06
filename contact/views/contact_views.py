from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True)

    context = {
        'contacts': contacts,
    }

    return render(
        request, 
        'contact/index.html',
        context=context
    )


def contact(request, contact_id):
    #single_contact = Contact.objects.get(id=contact_id)
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)
    context = {
        'contact': single_contact,
    }
    return render(
        request,
        'contact/contact.html',
        context       
    )
