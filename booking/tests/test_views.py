from django.test import TestCase, Client
from django.urls import reverse
from booking.models import (XrayAppointment, CtAppointment, MriAppointment,
                            MammoAppointment, DexaAppointment,
                            FluoroAppointment,
                            AngioAppointment, UsAppointment, NmAppointment)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_xray_appointment_GET(self):
        response = self.client.get(reverse('book_xray'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/xray.html')

    def test_ct_appointment_GET(self):
        response = self.client.get(reverse('book_ct'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/ct.html')

    def test_mri_appointment_GET(self):
        response = self.client.get(reverse('book_mri'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/mri.html')

    def test_mammo_appointment_GET(self):
        response = self.client.get(reverse('book_mammo'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/mammo.html')

    def test_dexa_appointment_GET(self):
        response = self.client.get(reverse('book_dexa'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/dexa.html')

    def test_fluoro_appointment_GET(self):
        response = self.client.get(reverse('book_fluoro'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/fluoro.html')
        
    def test_angio_appointment_GET(self):
        response = self.client.get(reverse('book_angio'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/angio.html')

    def test_ultrasound_appointment_GET(self):
        response = self.client.get(reverse('book_ultrasound'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/ultrasound.html')

    def test_nuclear_med_appointment_GET(self):
        response = self.client.get(reverse('book_nm'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/nm.html')
