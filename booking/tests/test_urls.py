from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import (HomeTemplateView,
                           PrivacyTemplateView, ContactTemplateView,
                           ThanksTemplateView,
                           BookXrayTemplateView, BookCtTemplateView,
                           BookMriTemplateView, BookDexaTemplateView,
                           BookMammoTemplateView, BookNmTemplateView,
                           BookAngioTemplateView, BookUltrasoundTemplateView,
                           BookFluoroTemplateView, InformationTemplateView,
                           RequestsTemplateView, LocationsTemplateView,
                           RequestsTemplateView, RadiationTemplateView,
                           ResultsTemplateView, DepartmentTemplateView,
                           ExamboardTemplateView, XrayTemplateView,
                           CtTemplateView,
                           MriTemplateView, UsTemplateView, NmTemplateView,
                           MammoTemplateView, FluoroTemplateView,
                           AngioTemplateView,
                           DexaTemplateView, Page500, Page404, Page403)


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeTemplateView)

    def test_contact_url_resolves(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactTemplateView)

    def test_privacy_url_resolves(self):
        response = self.client.get('/privacy')
        self.assertEqual(response.status_code, 200)

        url = reverse('privacy')
        self.assertEquals(resolve(url).func.view_class, PrivacyTemplateView)

    def test_403_url_resolves(self):
        response = self.client.get('/403')
        self.assertEqual(response.status_code, 200)

        url = reverse('403')
        self.assertEquals(resolve(url).func.view_class, Page403)

    def test_404_url_resolves(self):
        response = self.client.get('/404')
        self.assertEqual(response.status_code, 200)

        url = reverse('404')
        self.assertEquals(resolve(url).func.view_class, Page404)

    def test_500_url_resolves(self):
        response = self.client.get('/500')
        self.assertEqual(response.status_code, 200)

        url = reverse('500')
        self.assertEquals(resolve(url).func.view_class, Page500)

    def test_thanks_url_resolves(self):
        response = self.client.get('/thanks')
        self.assertEqual(response.status_code, 200)

        url = reverse('thanks')
        self.assertEquals(resolve(url).func.view_class, ThanksTemplateView)

    # TESTING BOOKING PAGES

    def test_book_xray_url_resolves(self):
        response = self.client.get('/book/xray')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_xray')
        self.assertEquals(resolve(url).func.view_class, BookXrayTemplateView)

    def test_book_ct_url_resolves(self):
        response = self.client.get('/book/ct')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_ct')
        self.assertEquals(resolve(url).func.view_class, BookCtTemplateView)

    def test_book_mri_url_resolves(self):
        response = self.client.get('/book/mri')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_mri')
        self.assertEquals(resolve(url).func.view_class, BookMriTemplateView)

    def test_book_ultrasound_url_resolves(self):
        response = self.client.get('/book/ultrasound')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_ultrasound')
        self.assertEquals(resolve(url).func.view_class, BookUltrasoundTemplateView)

    def test_book_mammo_url_resolves(self):
        response = self.client.get('/book/mammo')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_mammo')
        self.assertEquals(resolve(url).func.view_class, BookMammoTemplateView)

    def test_book_nm_url_resolves(self):
        response = self.client.get('/book/nm')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_nm')
        self.assertEquals(resolve(url).func.view_class, BookNmTemplateView)

    def test_book_angio_url_resolves(self):
        response = self.client.get('/book/angio')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_angio')
        self.assertEquals(resolve(url).func.view_class, BookAngioTemplateView)

    def test_book_fluoro_url_resolves(self):
        response = self.client.get('/book/fluoro')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_fluoro')
        self.assertEquals(resolve(url).func.view_class, BookFluoroTemplateView)

    def test_book_dexa_url_resolves(self):
        response = self.client.get('/book/dexa')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_dexa')
        self.assertEquals(resolve(url).func.view_class, BookDexaTemplateView)

    # TESTING MODALITY INFORMATION PAGES

    def test_exam_board_url_resolves(self):
        response = self.client.get('/examinations')
        self.assertEqual(response.status_code, 200)

        url = reverse('examinations')
        self.assertEquals(resolve(url).func.view_class, ExamboardTemplateView)

    def test_info_xray_url_resolves(self):
        response = self.client.get('/examinations/xray')
        self.assertEqual(response.status_code, 200)

        url = reverse('xray')
        self.assertEquals(resolve(url).func.view_class, XrayTemplateView)

    def test_info_ct_url_resolves(self):
        response = self.client.get('/examinations/computed_tomography')
        self.assertEqual(response.status_code, 200)

        url = reverse('computed_tomography')
        self.assertEquals(resolve(url).func.view_class, CtTemplateView)

    def test_info_mri_url_resolves(self):
        response = self.client.get('/examinations/magnetic_resonance')
        self.assertEqual(response.status_code, 200)

        url = reverse('magnetic_resonance')
        self.assertEquals(resolve(url).func.view_class, MriTemplateView)

    def test_info_ultrasound_url_resolves(self):
        response = self.client.get('/examinations/ultrasound')
        self.assertEqual(response.status_code, 200)

        url = reverse('ultrasound')
        self.assertEquals(resolve(url).func.view_class, UsTemplateView)

    def test_info_mammo_url_resolves(self):
        response = self.client.get('/examinations/mammography')
        self.assertEqual(response.status_code, 200)

        url = reverse('mammography')
        self.assertEquals(resolve(url).func.view_class, MammoTemplateView)

    def test_info_nm_url_resolves(self):
        response = self.client.get('/examinations/nuclear_medicine')
        self.assertEqual(response.status_code, 200)

        url = reverse('nuclear_medicine')
        self.assertEquals(resolve(url).func.view_class, NmTemplateView)

    def test_info_angio_url_resolves(self):
        response = self.client.get('/examinations/angiography')
        self.assertEqual(response.status_code, 200)

        url = reverse('angiography')
        self.assertEquals(resolve(url).func.view_class, AngioTemplateView)

    def test_info_fluoro_url_resolves(self):
        response = self.client.get('/examinations/fluoroscopy')
        self.assertEqual(response.status_code, 200)

        url = reverse('fluoroscopy')
        self.assertEquals(resolve(url).func.view_class, FluoroTemplateView)

    def test_info_dexa_url_resolves(self):
        response = self.client.get('/examinations/dexa')
        self.assertEqual(response.status_code, 200)

        url = reverse('dexa')
        self.assertEquals(resolve(url).func.view_class, DexaTemplateView)

    # TESTING INFORMATION PAGES

    def test_info_board_url_resolves(self):
        response = self.client.get('/information')
        self.assertEqual(response.status_code, 200)

        url = reverse('information')
        self.assertEquals(resolve(url).func.view_class, InformationTemplateView)

    def test_info_requests_url_resolves(self):
        response = self.client.get('/information/requests')
        self.assertEqual(response.status_code, 200)

        url = reverse('requests')
        self.assertEquals(resolve(url).func.view_class, RequestsTemplateView)

    def test_info_results_url_resolves(self):
        response = self.client.get('/information/results')
        self.assertEqual(response.status_code, 200)

        url = reverse('results')
        self.assertEquals(resolve(url).func.view_class, ResultsTemplateView)

    def test_info_radiation_url_resolves(self):
        response = self.client.get('/information/radiation')
        self.assertEqual(response.status_code, 200)

        url = reverse('radiation')
        self.assertEquals(resolve(url).func.view_class, RadiationTemplateView)

    def test_info_locations_url_resolves(self):
        response = self.client.get('/information/locations')
        self.assertEqual(response.status_code, 200)

        url = reverse('locations')
        self.assertEquals(resolve(url).func.view_class, LocationsTemplateView)

    def test_info_department_url_resolves(self):
        response = self.client.get('/information/department')
        self.assertEqual(response.status_code, 200)

        url = reverse('department')
        self.assertEquals(resolve(url).func.view_class, DepartmentTemplateView)
