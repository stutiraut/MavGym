from django.db import models
from django.utils import timezone


time = (
    ('7:00 am - 8:00 am', '7:00 am - 8:00 am'),
    ('8:00 am - 9:00 am', '8:00 am - 9:00 am'),
    ('9:00 am - 10:00 am', '9:00 am - 10:00 am'),
    ('10:00 am - 11:00 am', '10:00 am - 11:00 am'),
    ('11:00 am - 12:00 pm', '11:00 am - 12:00 pm'),
    ('12:00 pm - 1:00 pm', '12:00 pm - 1:00 pm'),
    ('1:00 pm - 2:00 pm', '1:00 pm - 2:00 pm'),
    ('2:00 pm - 3:00 pm', '2:00 pm - 3:00 pm'),
    ('3:00 pm - 4:00 pm', '3:00 pm - 4:00 pm'),
    ('4:00 pm - 5:00 pm', '4:00 pm - 5:00 pm'),

)

status =(

    ('available', 'AVAILABLE'),
    ('cancelled', 'CANCELLED'),

    )

size =(

    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),

    )

issue=(
    ('issue', 'ISSUE'),
    ('issue pending', 'ISSUE PENDING'),
    ('issued', 'ISSUED')
)

# Create your models here.
# Staff module
class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_street = models.CharField(max_length=50)
    staff_city = models.CharField(max_length=50)
    staff_state = models.CharField(max_length=50)
    staff_zip = models.CharField(max_length=10)
    staff_email = models.CharField(max_length=50)
    staff_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.staff_name)


# Customer module
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_street = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_state = models.CharField(max_length=50)
    customer_zip = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_name)

class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    activity_status=models.CharField(max_length=100, choices=status, blank=True)
    date = models.DateField(blank=True, default=timezone.now)
    time = models.CharField(max_length=100, choices=time)
    created_date = models.DateField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.activity_name)


# Equipment model
class Equipment(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='equips')
    equipment_name = models.CharField(max_length=50)
    equipment_description = models.TextField()
    equipment_size = models.CharField(max_length=100, choices=size)
    equipment_issue_status = models.CharField(max_length=100, choices=issue)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_name)


