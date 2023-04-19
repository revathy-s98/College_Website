from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Member(models.Model):
#     firstname = models.CharField(max_length=124)
#     lastname = models.CharField(max_length=124)
    birthdate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    age = models.IntegerField(blank=True, null=True)
#     GENDER_COICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#     gender = models.CharField(max_length=3, choices=GENDER_COICES,
#                               default="N/A")
    phonenumber = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=125)
    address = models.CharField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


