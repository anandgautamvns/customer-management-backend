from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils import timezone
from datetime import date

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(120)]  # Restrict age range
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex=r'^\+?\d{7,15}$', message="Enter a valid phone number.")]
    )
    email = models.EmailField(unique=True, null=True, blank=True)  # Allows optional emails
    # email = models.EmailField(unique=True, null=True, blank=True, default="temp@example.com")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField(
        null=False,
        validators=[MaxValueValidator(date.today)]  # Prevent future dates
    )
    is_employee = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)  # Updates automatically on modification

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_gender_display()})"

    class Meta:
        ordering = ["-created_at"]  # Orders by latest created first