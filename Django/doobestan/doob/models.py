from django.db import models


class DeliveryReport(models.Model):
    phone_number = models.CharField(max_length=200)


class Hospital(models.Model):
    name = models.CharField(max_length=200, unique=True)
    manager_name = models.CharField(max_length=200, default='')
    manager_id = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    manager_name = models.CharField(max_length=200, default='')
    manager_id = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Sick(models.Model):
    name = models.CharField(max_length=200, default='')
    nationalID = models.CharField(max_length=200)
    illName = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, related_name='sicks', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'({self.name}, {self.nationalID})'


class Employee(models.Model):
    name = models.CharField(max_length=200, default='')
    nationalID = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.name}, {self.nationalID})'


