from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from .forms import ContactForm
from .actions import CreateContactInfo

class ContactPage(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def form_valid(self, form):
        CreateContactInfo().create(
            name = form.data.get('name'),
            surname = form.data.get('surname'),
            email = form.data.get('email'),
            number = form.data.get('number')
        )
        return HttpResponseRedirect(self.get_success_url())
        


