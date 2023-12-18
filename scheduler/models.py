import random
import string

from django.db import models


# Function to generate a unique ID using random characters
def generate_unique_id():
    # Generate a unique ID using random characters
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


# Model to represent people with roles
class People(models.Model):
    role_choices = [
        ("ENG", "Engineer"),
        ("PM", "Program Manager"),
        ("OP", "Operator"),
        ("MT", "Maintenance"),
    ]
    key = models.AutoField(primary_key=True, editable=False)
    label = models.CharField(max_length=120)
    priority = models.SmallIntegerField(default=0)
    role = models.CharField(max_length=3, choices=role_choices, default="ENG")

    def __str__(self):
        return self.label


# Model to represent tester sections
class TesterSection(models.Model):
    keyTesterSection = models.CharField(
        primary_key=True, default=generate_unique_id, unique=True, max_length=10
    )
    label = models.CharField(max_length=120)
    open = models.BooleanField(default=False)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="testerselections",
    )
    priority = models.IntegerField(default=0)

    # level = models.SmallIntegerField()
    def __str__(self):
        return self.label


# Model to represent testers
class Tester(models.Model):
    key = models.CharField(
        primary_key=True, default=generate_unique_id, unique=True, max_length=10
    )
    label = models.CharField(max_length=120)
    parent = models.ForeignKey(
        TesterSection, on_delete=models.SET_NULL, null=True, related_name="testers"
    )
    priority = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.label


# Model to represent customers
class Customer(models.Model):
    key = models.AutoField(primary_key=True, editable=False)
    label = models.CharField(max_length=120)

    def __str__(self):
        return self.label


# Model to represent devices
class Device(models.Model):
    key = models.AutoField(primary_key=True, editable=False)
    label = models.CharField(max_length=120)

    def __str__(self):
        return self.label


# Model to represent scheduled time slots
class Event(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    text = models.CharField(blank=True, max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # timestamp = models.DateTimeField(auto_now_add=True)
    tester = models.ForeignKey(
        Tester, on_delete=models.SET_NULL, null=True, related_name="events"
    )
    person = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, related_name="events"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="events",
        blank=True,
    )
    job_number = models.CharField(max_length=120, blank=True)
    device = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, related_name="events", blank=True
    )
    locked = models.BooleanField(default=False)
    window_lot = models.BooleanField(default=False)
    number_units = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    dep_choices = [
        ("ENG", "Engineer"),
        ("PROD", "Production"),
        ("CAL", "Calibration"),
        ("MT", "Maintenance"),
    ]
    department = models.CharField(max_length=4, choices=dep_choices, default="PROD")
    steps = models.CharField(max_length=120, blank=True)
    peripherals = models.CharField(max_length=120, blank=True)
    test_temps = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.text
