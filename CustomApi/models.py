from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class userLoanData(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduate', 'Graduated'),
        ('Not_Graduate', 'Not_Graduate')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )
    firstname = models.CharField(max_length=18)
    lastname = models.CharField(max_length=18)
    dependants = models.IntegerField(default=0)
    applicantincome = models.IntegerField(default=0)
    coapplicatincome = models.IntegerField(default=0)
    loanamt = models.IntegerField(default=0)
    loanterm = models.IntegerField(default=0)
    credithistory = models.IntegerField(default=0)
    gender = models.CharField(max_length=18, choices=GENDER_CHOICES)
    married = models.CharField(max_length=18, choices=MARRIED_CHOICES)
    graduatededucation = models.CharField(
        max_length=18, choices=GRADUATED_CHOICES)
    selfemployed = models.CharField(
        max_length=18, choices=SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=18, choices=PROPERTY_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.lastname, self.firstname)


class Account(AbstractBaseUser):
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )
    USERNAME_FIELD = "uid"
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(verbose_name="password", max_length=128)
    approved = models.BooleanField(default=None, null=True)
    loanData = models.OneToOneField(
        userLoanData,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email
