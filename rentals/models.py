from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fuel_tag = models.CharField(max_length=20, default="PETROL ONLY")
    price_12_hours = models.IntegerField()
    price_24_hours = models.IntegerField()
    km_limit_12h = models.IntegerField(default=150)
    km_limit_24h = models.IntegerField(default=250)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=15)
    pickup_date = models.DateField()
    rental_mode = models.CharField(max_length=20)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"