from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'

class ContactTemplateView(TemplateView, POST):
    template_name = 'contact.html'
    
    def contact(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            send_mail(name, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return render(request, 'thanks.html', {"email":email})
        return render(request, 'contact.html', {})

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
