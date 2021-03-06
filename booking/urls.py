
from django.urls import path

from .views import (HomeTemplateView,
                    PrivacyTemplateView, ContactTemplateView,
                    ThanksTemplateView, ManageTemplateView,
                    BookXrayTemplateView, BookCtTemplateView,
                    BookMriTemplateView, BookDexaTemplateView,
                    BookMammoTemplateView, BookNmTemplateView,
                    BookAngioTemplateView, BookUltrasoundTemplateView,
                    BookFluoroTemplateView, InformationTemplateView,
                    RequestsTemplateView, LocationsTemplateView,
                    RequestsTemplateView, RadiationTemplateView,
                    ResultsTemplateView, DepartmentTemplateView,
                    ExamboardTemplateView, XrayTemplateView, CtTemplateView,
                    MriTemplateView, UsTemplateView, NmTemplateView,
                    MammoTemplateView, FluoroTemplateView, AngioTemplateView,
                    DexaTemplateView, Page500, Page404, Page403,
                    WorklistTemplateView)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('privacy', PrivacyTemplateView.as_view(), name='privacy'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
    path('thanks', ThanksTemplateView.as_view(), name='thanks'),
    path('manage', ManageTemplateView.as_view(), name='manage'),
    path('worklist', WorklistTemplateView.as_view(), name='worklist'),

    path('book/xray', BookXrayTemplateView.as_view(), name='book_xray'),
    path('book/ct', BookCtTemplateView.as_view(), name='book_ct'),
    path('book/mri', BookMriTemplateView.as_view(), name='book_mri'),
    path('book/ultrasound', BookUltrasoundTemplateView.as_view(), name='book_ultrasound'),
    path('book/nm', BookNmTemplateView.as_view(), name='book_nm'),
    path('book/dexa', BookDexaTemplateView.as_view(), name='book_dexa'),
    path('book/angio', BookAngioTemplateView.as_view(), name='book_angio'),
    path('book/fluoro', BookFluoroTemplateView.as_view(), name='book_fluoro'),
    path('book/mammo', BookMammoTemplateView.as_view(), name='book_mammo'),

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

    path('403', Page403.as_view(), name='403'),
    path('404', Page404.as_view(), name='404'),
    path('500', Page500.as_view(), name='500'),
]
