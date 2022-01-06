from django.db import models

# Create your models here.


class XrayAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    examination_type = models.CharField(max_length=100)
    exam_location = models.CharField(max_length=100)
    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class CtAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    examination_type = models.CharField(max_length=100)
    exam_location = models.CharField(max_length=100)
    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)
    weight_status = models.CharField(max_length=100)
    kidney_status = models.CharField(max_length=100)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class MriAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    examination_type = models.CharField(max_length=100)
    exam_location = models.CharField(max_length=100)
    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)
    weight_status = models.CharField(max_length=100)
    kidney_status = models.CharField(max_length=100)
    metal_status = models.CharField(max_length=100)
    pacemaker_status = models.CharField(max_length=100)
    eyes_status = models.CharField(max_length=100)
    claustrophobia_status = models.CharField(max_length=100)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class FluoroAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    examination_type = models.CharField(max_length=100)
    exam_location = models.CharField(max_length=100)
    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)
    weight_status = models.CharField(max_length=100)
    kidney_status = models.CharField(max_length=100)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class AngioAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    examination_type = models.CharField(max_length=100)

    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)
    weight_status = models.CharField(max_length=100)
    kidney_status = models.CharField(max_length=100)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']


class DexaAppointment(models.Model):
    request_number = models.CharField(max_length=10)
    hospital_number = models.CharField(max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    date_of_exam = models.DateField()
    time_of_exam = models.TimeField()

    preg_status = models.CharField(max_length=20)
    weight_status = models.CharField(max_length=100)
    surgery_status = models.CharField(max_length=100)

    comms_problems = models.TextField(max_length=1000)
    contact_number = models.IntegerField()

    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']