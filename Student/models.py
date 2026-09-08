from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('BBA', 'BBA'),
        ('B.Com', 'B.Com'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
    ]

    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.student_name