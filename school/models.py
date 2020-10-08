from django.db import models

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Student(models.Model):
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    course = models.CharField(max_length=40)
    Stream = models.CharField(max_length=40)
    admission_id = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_no = models.DecimalField(max_digits=10,decimal_places=0)
    Stream = models.CharField(max_length=40)
    identity = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

