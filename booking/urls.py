
from django.urls import path
from .views import HomeTemplateView, PrivacyTemplateView, ContactTemplateView, AdminTemplateView, InformationTemplateView, RequestsTemplateView, LocationsTemplateView, RequestsTemplateView, RadiationTemplateView, ResultsTemplateView, DepartmentTemplateView, ExamboardTemplateView, XrayTemplateView, CtTemplateView, MriTemplateView, UsTemplateView, NmTemplateView, MammoTemplateView, FluoroTemplateView, AngioTemplateView, DexaTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('privacy', PrivacyTemplateView.as_view(), name='privacy'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
    path('admin/login/?next=/admin/', AdminTemplateView.as_view(), name='admin'),


    

    path('information', InformationTemplateView.as_view(), name='information'),
    path('information/requests', RequestsTemplateView.as_view(), name='requests'),
    path('information/locations', LocationsTemplateView.as_view(), name='locations'),
    path('information/radiation', RadiationTemplateView.as_view(), name='radiation'),
    path('information/results', ResultsTemplateView.as_view(), name='results'),
    path('information/department', DepartmentTemplateView.as_view(), name='department'),

    path('examinations', ExamboardTemplateView.as_view(), name='examinations'),
    path('examinations/xray', XrayTemplateView.as_view(), name='xray'),
    path('examinations/computed_tomography', CtTemplateView.as_view(), name='computed_tomography'),
    path('examinations/magnetic_resonance', MriTemplateView.as_view(), name='magnetic_resonance'),
    path('examinations/ultrasound', UsTemplateView.as_view(), name='ultrasound'),
    path('examinations/mammography', MammoTemplateView.as_view(), name='mammography'),
    path('examinations/nuclear_medicine', NmTemplateView.as_view(), name='nuclear_medicine'),
    path('examinations/fluoroscopy', FluoroTemplateView.as_view(), name='fluoroscopy'),
    path('examinations/angiography', AngioTemplateView.as_view(), name='angiography'),
    path('examinations/dexa', DexaTemplateView.as_view(), name='dexa'),
]
