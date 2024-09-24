from django.db import models

class Car(models.Model):
    MAKE_CHOICES = [
        ('TOYOTA', 'Toyota'),
        ('HONDA', 'Honda'),
        ('FORD', 'Ford'),
        ('LEXUS', 'Lexus'),
        ('CHEVROLET', 'Chevrolet'),
        ('BMW', 'Bmw'),
        ('MERCEDES-BENZ', 'Mercedes-benz'),
        ('MAZDA', 'Mazda'),
        ('AUDI', 'Audi'),
        ('KIA', 'Kia'),
        ('HYUNDAI', 'Hyundai'),
        ('NISSAN', 'Nissan'),
        ('VOLKSWAGEN', 'Volkswagen'),
    ]

    LHD_RHD_CHOICES = [
        ('LHD', 'Left-Hand drive'),
        ('RHD', 'Right-Hand drive'),
    ]

    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    engine = models.DecimalField(max_digits=10, decimal_places=1)
    rhd_lhd = models.CharField(max_length=3, choices=LHD_RHD_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'