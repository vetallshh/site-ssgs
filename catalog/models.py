from django.db import models
from django.urls import reverse
import uuid

class ReestrActive(models.Model):
    urIp = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    lessName = models.CharField(max_length=100)
    statusChlena = models.CharField(max_length=100)
    regNumber = models.CharField(max_length=100)
    dataReg = models.CharField(max_length=100)
    dataEnd = models.CharField(max_length=100)
    osnEndChlenstv = models.CharField(max_length=100)
    ogrn = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    dataGosReg = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telNumber = models.CharField(max_length=50)
    adresIndex = models.CharField(max_length=100)
    adressStrana = models.CharField(max_length=100)
    adressSubject = models.CharField(max_length=100)
    adresRayon = models.CharField(max_length=100)
    adresNasPunkt = models.CharField(max_length=100)
    adresUlits = models.CharField(max_length=100)
    adressDom = models.CharField(max_length=100)
    adressKorps = models.CharField(max_length=100)
    adressPomesh = models.CharField(max_length=100)
    rukovoditel = models.CharField(max_length=100)
    fio = models.CharField(max_length=100)
    svedOSootvetstvi = models.CharField(max_length=100)
    kfSro = models.CharField(max_length=100)
    razmerVznosa = models.CharField(max_length=100)
    urovOtvetstv = models.CharField(max_length=100)
    razmerVznOdo = models.CharField(max_length=100)
    urovenOtvenstvnOdo = models.CharField(max_length=100)


    def __str__(self):
        return self.fullName