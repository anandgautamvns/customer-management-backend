from rest_framework import serializers
from .models import Customer
from datetime import date


class CustomerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)  # Ensure age is calculated

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name', 'dob', 'phone_number', 'age',
            'email', 'gender', 'is_employee', 'created_at', 'modified_at'
        ]
        extra_kwargs = {
            'email': {'required': False},  # Allows email to be optional
            'phone_number': {'required': True},
            'dob': {'required': True},
        }

    def get_age(self, obj):
        """Calculate age based on date of birth (dob)."""
        today = date.today()
        return today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))

    def validate_dob(self, value):
        """Ensure the date of birth is not in the future."""
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def validate_phone_number(self, value):
        """Ensure phone number follows international format."""
        if not value.startswith("+") and not value.isdigit():
            raise serializers.ValidationError("Phone number must be numeric and may start with '+'.")
        return value

    def validate_email(self, value):
        """Ensure email is unique if provided."""
        if value and Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value