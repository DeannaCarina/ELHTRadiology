from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core import mail
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib import messages
from .models import XrayAppointment, CtAppointment, MriAppointment, FluoroAppointment, AngioAppointment, DexaAppointment, MammoAppointment, NmAppointment, UsAppointment

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
                send_mail(
                    subject=f"New message from ELHT RBS",
                    message=f"You sent a message to ELHT Radiology Booking service, we aim to respond within 24 hours. Here is what you sent:\n\nSubject: {subject}\n\nMessage: {message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email])
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

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')
        exam_location = request.POST.get('examination_location')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an x-ray appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for x-ray via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        xray_appointment = XrayAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,
            exam_location=exam_location,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        xray_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at {exam_location} for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)


class BookCtTemplateView(TemplateView):
    template_name = 'book/ct.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')
        exam_location = request.POST.get('examination_location')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        kidney_status = request.POST.get('kidney_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a CT appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for CT via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        ct_appointment = CtAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,
            exam_location=exam_location,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            kidney_status=kidney_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        ct_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at {exam_location} for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookMriTemplateView(TemplateView):
    template_name = 'book/mri.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')
        exam_location = request.POST.get('examination_location')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        kidney_status = request.POST.get('kidney_status')
        metal_status = request.POST.get('metal_status')
        pacemaker_status = request.POST.get('pacemaker_status')
        eyes_status = request.POST.get('eyes_status')
        claustrophobia_status = request.POST.get('claustrophobia_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an MRI appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for MRI via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        mri_appointment = MriAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,
            exam_location=exam_location,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            kidney_status=kidney_status,
            metal_status=metal_status,
            pacemaker_status=pacemaker_status,
            eyes_status=eyes_status,
            claustrophobia_status=claustrophobia_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        mri_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at {exam_location} for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookDexaTemplateView(TemplateView):
    template_name = 'book/dexa.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        surgery_status = request.POST.get('surgery_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Dexa appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Accrington Victoria Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for dexa via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        dexa_appointment = DexaAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            surgery_status=surgery_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        dexa_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at Accrington Victoria Hospital for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookMammoTemplateView(TemplateView):
    template_name = 'book/mammo.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        implants_status = request.POST.get('implants_status')
        screening_status = request.POST.get('screening_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Mammography appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Burnley General Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for Mammography via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        mammo_appointment = MammoAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            implants_status=implants_status,
            screening_status=screening_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        mammo_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at Burnley General Hospital for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookNmTemplateView(TemplateView):
    template_name = 'book/nm.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')

        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')

        preg_status = request.POST.get('preg_status')
        breastfeeding_status = request.POST.get('breastfeeding_status')
        weight_status = request.POST.get('weight_status')
        kidney_status = request.POST.get('kidney_status')

        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Nuclear Medicine appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Royal Blackburn Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for Nuclear Medicine via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        nm_appointment = NmAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,

            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            breastfeeding_status=breastfeeding_status,
            weight_status=weight_status,
            kidney_status=kidney_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        nm_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at Royal Blackburn Hospital for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookAngioTemplateView(TemplateView):
    template_name = 'book/angio.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')

        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        kidney_status = request.POST.get('kidney_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an Angiography appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Royal Blackburn Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for Angiography via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        angio_appointment = AngioAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,

            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            kidney_status=kidney_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        angio_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at Royal Blackburn Hospital for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookUltrasoundTemplateView(TemplateView):
    template_name = 'book/ultrasound.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')
        exam_location = request.POST.get('examination_location')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an Ultrasound appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for Ultrasound via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        us_appointment = UsAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,
            exam_location=exam_location,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        us_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at {exam_location} for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

class BookFluoroTemplateView(TemplateView):
    template_name = 'book/fluoro.html'

    def post(self, request):
        request_number = request.POST.get('request_number')
        hospital_number = request.POST.get('hospital_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        examination_type = request.POST.get('examination_type')
        exam_location = request.POST.get('examination_location')
        date_of_exam = request.POST.get('date_of_exam')
        time_of_exam = request.POST.get('time_of_exam')
        preg_status = request.POST.get('preg_status')
        weight_status = request.POST.get('weight_status')
        kidney_status = request.POST.get('kidney_status')
        comms_problems = request.POST.get('comms_problems')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Fluoroscopy appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_address])
                send_mail(
                    subject=f"New booking via ELHT RBS",
                    message=f"{first_name} {last_name} just made a booking for Fluoroscopy via ELHT RBS. Log in to admin page to confirm this booking.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        fluoro_appointment = FluoroAppointment.objects.create(
            request_number=request_number,
            hospital_number=hospital_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            examination_type=examination_type,
            exam_location=exam_location,
            date_of_exam=date_of_exam,
            time_of_exam=time_of_exam,
            preg_status=preg_status,
            weight_status=weight_status,
            kidney_status=kidney_status,
            comms_problems=comms_problems,
            contact_number=contact_number,
            email_address=email_address
        )

        fluoro_appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. Your examination has been booked at {exam_location} for {date_of_exam} at {time_of_exam}. If you are unable to make your appointment please let us know as soon as possible.")
        return HttpResponseRedirect(request.path)

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

# Classes for error pages

class Page404(TemplateView):
    template_name = '404.html'

class Page500(TemplateView):
    template_name = '500.html'

class Page403(TemplateView):
    template_name = '403.html'