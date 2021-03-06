from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core import mail
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib import messages
import datetime
import time
from .models import XrayAppointment, CtAppointment, MriAppointment, FluoroAppointment, AngioAppointment, DexaAppointment, MammoAppointment, NmAppointment, UsAppointment
from django.contrib.auth.decorators import login_required

class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class ManageTemplateView(TemplateView):
    template_name = 'manage.html'
    login_required = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        ctappointments = CtAppointment.objects.all()
        xrayappointments = XrayAppointment.objects.all()
        mriappointments = MriAppointment.objects.all()
        usappointments = UsAppointment.objects.all()
        mammoappointments = MammoAppointment.objects.all()
        dexaappointments = DexaAppointment.objects.all()
        nmappointments = NmAppointment.objects.all()
        angioappointments = AngioAppointment.objects.all()
        fluoroappointments = FluoroAppointment.objects.all()
        
        context.update({
            "ctappointments":ctappointments,
            "xrayappointments":xrayappointments,
            "mriappointments":mriappointments,
            "usappointments":usappointments,
            "mammoappointments":mammoappointments,
            "dexaappointments":dexaappointments,
            "nmappointments":nmappointments,
            "angioappointments":angioappointments,
            "fluoroappointments":fluoroappointments,
        })
        return context

    def post(self, request):
        if request.POST.get("form_type") == 'xrayform':
            ref_number = request.POST.get("ref_number")
            xrayappointment = XrayAppointment.objects.get(ref_number=ref_number)
            xrayappointment.accepted = True
            xrayappointment.accepted_date = datetime.datetime.now()
            xrayappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'ctform':
            ref_number = request.POST.get("ref_number")
            ctappointment = CtAppointment.objects.get(ref_number=ref_number)
            ctappointment.accepted = True
            ctappointment.accepted_date = datetime.datetime.now()
            ctappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'mriform':
            ref_number = request.POST.get("ref_number")
            mriappointment = MriAppointment.objects.get(ref_number=ref_number)
            mriappointment.accepted = True
            mriappointment.accepted_date = datetime.datetime.now()
            mriappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'usform':
            ref_number = request.POST.get("ref_number")
            usappointment = UsAppointment.objects.get(ref_number=ref_number)
            usappointment.accepted = True
            usappointment.accepted_date = datetime.datetime.now()
            usappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'mammoform':
            ref_number = request.POST.get("ref_number")
            mammoappointment = MammoAppointment.objects.get(ref_number=ref_number)
            mammoappointment.accepted = True
            mammoappointment.accepted_date = datetime.datetime.now()
            mammoappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'dexaform':
            ref_number = request.POST.get("ref_number")
            dexaappointment = DexaAppointment.objects.get(ref_number=ref_number)
            dexaappointment.accepted = True
            dexaappointment.accepted_date = datetime.datetime.now()
            dexaappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'nmform':
            ref_number = request.POST.get("ref_number")
            nmappointment = NmAppointment.objects.get(ref_number=ref_number)
            nmappointment.accepted = True
            nmappointment.accepted_date = datetime.datetime.now()
            nmappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'angioform':
            ref_number = request.POST.get("ref_number")
            angioappointment = AngioAppointment.objects.get(ref_number=ref_number)
            angioappointment.accepted = True
            angioappointment.accepted_date = datetime.datetime.now()
            angioappointment.save()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'fluoroform':
            ref_number = request.POST.get("ref_number")
            fluoroappointment = FluoroAppointment.objects.get(ref_number=ref_number)
            fluoroappointment.accepted = True
            fluoroappointment.accepted_date = datetime.datetime.now()
            fluoroappointment.save()
            return HttpResponseRedirect(request.path)


class WorklistTemplateView(TemplateView):
    template_name = 'worklist.html'
    login_required = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        ctappointments = CtAppointment.objects.all()
        xrayappointments = XrayAppointment.objects.all()
        mriappointments = MriAppointment.objects.all()
        usappointments = UsAppointment.objects.all()
        mammoappointments = MammoAppointment.objects.all()
        dexaappointments = DexaAppointment.objects.all()
        nmappointments = NmAppointment.objects.all()
        angioappointments = AngioAppointment.objects.all()
        fluoroappointments = FluoroAppointment.objects.all()
        
        context.update({
            "ctappointments":ctappointments,
            "xrayappointments":xrayappointments,
            "mriappointments":mriappointments,
            "usappointments":usappointments,
            "mammoappointments":mammoappointments,
            "dexaappointments":dexaappointments,
            "nmappointments":nmappointments,
            "angioappointments":angioappointments,
            "fluoroappointments":fluoroappointments,
        })
        return context

    def post(self, request):
        if request.POST.get("form_type") == 'xrayform':
            ref_number = request.POST.get("ref_number")
            xrayappointment = XrayAppointment.objects.get(ref_number=ref_number)
            xrayappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'ctform':
            ref_number = request.POST.get("ref_number")
            ctappointment = CtAppointment.objects.get(ref_number=ref_number)
            ctappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'mriform':
            ref_number = request.POST.get("ref_number")
            mriappointment = MriAppointment.objects.get(ref_number=ref_number)
            mriappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'usform':
            ref_number = request.POST.get("ref_number")
            usappointment = UsAppointment.objects.get(ref_number=ref_number)
            usappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'mammoform':
            ref_number = request.POST.get("ref_number")
            mammoappointment = MammoAppointment.objects.get(ref_number=ref_number)
            mammoappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'dexaform':
            ref_number = request.POST.get("ref_number")
            dexaappointment = DexaAppointment.objects.get(ref_number=ref_number)
            dexaappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'nmform':
            ref_number = request.POST.get("ref_number")
            nmappointment = NmAppointment.objects.get(ref_number=ref_number)
            nmappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'angioform':
            ref_number = request.POST.get("ref_number")
            angioappointment = AngioAppointment.objects.get(ref_number=ref_number)
            angioappointment.delete()
            return HttpResponseRedirect(request.path)
        elif request.POST.get("form_type") == 'fluoroform':
            ref_number = request.POST.get("ref_number")
            fluoroappointment = FluoroAppointment.objects.get(ref_number=ref_number)
            fluoroappointment.delete()
            return HttpResponseRedirect(request.path)
        


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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"XR{last_name}{epoch}"

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an x-ray appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"CT{last_name}{epoch}"

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an CT appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"MR{last_name}{epoch}"

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an MRI appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"DX{last_name}{epoch}"

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a dexa appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Accrington Victoria Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"MA{last_name}{epoch}"

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Mammography appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Burnley General Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"NM{last_name}{epoch}"

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Nuclear Medicine appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Royal Blackburn Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"AN{last_name}{epoch}"

        if first_name and last_name and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an Angiography appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: Royal Blackburn Hospital. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"US{last_name}{epoch}"

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked an Ultrasound appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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

        date_time = f"{date_of_exam} {time_of_exam}"
        pattern = '%Y-%m-%d %H:%M'
        epoch = int(time.mktime(time.strptime(date_time, pattern)))

        ref_number = f"FL{last_name}{epoch}"

        if first_name and last_name and exam_location and date_of_exam and time_of_exam:
            try:
                send_mail(
                    subject=f"Your radiology appointment",
                    message=f"{first_name} {last_name},\n\nYou booked a Fluoroscopy appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
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
            email_address=email_address,
            ref_number=ref_number,
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
