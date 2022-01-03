from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core import mail
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
# from django.views.decorators.csrf import csrf_protect

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and message:
            try:
                send_mail(
                    subject=f"New message from {name} via ELHT RBS",
                    message=f"Subject: {subject}\n\nMessage: {message}\n\nPlease contact {name} on {email}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thanks')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')



class ThanksTemplateView(TemplateView):
    template_name = 'thanks.html'

class AdminTemplateView(TemplateView):
    template_name = 'admin.html'

# Classes for booking pages

class BookXrayTemplateView(TemplateView):
    template_name = 'book/xray.html'

class BookCtTemplateView(TemplateView):
    template_name = 'book/ct.html'

class BookMriTemplateView(TemplateView):
    template_name = 'book/mri.html'

class BookDexaTemplateView(TemplateView):
    template_name = 'book/dexa.html'

class BookMammoTemplateView(TemplateView):
    template_name = 'book/mammo.html'

class BookNmTemplateView(TemplateView):
    template_name = 'book/nm.html'

class BookAngioTemplateView(TemplateView):
    template_name = 'book/angio.html'

class BookUltrasoundTemplateView(TemplateView):
    template_name = 'book/ultrasound.html'

class BookFluoroTemplateView(TemplateView):
    template_name = 'book/fluoro.html'

# Classes for information pages

class InformationTemplateView(TemplateView):
    template_name = 'information/information.html'

class RequestsTemplateView(TemplateView):
    template_name = 'information/requests.html'

class LocationsTemplateView(TemplateView):
    template_name = 'information/locations.html'

class RadiationTemplateView(TemplateView):
    template_name = 'information/radiation.html'

class ResultsTemplateView(TemplateView):
    template_name = 'information/results.html'

class DepartmentTemplateView(TemplateView):
    template_name = 'information/department.html'

# Classes for examination pages

class ExamboardTemplateView(TemplateView):
    template_name = 'examinations/examinations.html'

class XrayTemplateView(TemplateView):
    template_name = 'examinations/xray.html'

class CtTemplateView(TemplateView):
    template_name = 'examinations/computed_tomography.html'

class MriTemplateView(TemplateView):
    template_name = 'examinations/magnetic_resonance.html'

class NmTemplateView(TemplateView):
    template_name = 'examinations/nuclear_medicine.html'

class MammoTemplateView(TemplateView):
    template_name = 'examinations/mammography.html'

class AngioTemplateView(TemplateView):
    template_name = 'examinations/angiography.html'

class UsTemplateView(TemplateView):
    template_name = 'examinations/ultrasound.html'

class FluoroTemplateView(TemplateView):
    template_name = 'examinations/fluoroscopy.html'

class DexaTemplateView(TemplateView):
    template_name = 'examinations/dexa.html'
