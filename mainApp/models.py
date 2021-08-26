
from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)


def __str__(self):
    return self.full_name



class Package(models.Model):
    title = models.CharField(max_length=210)

    def __str__(self):
        return self.title


class Gig(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    gig_title = models.CharField(max_length=520)
    packages = models.ManyToManyField(Package, through='GigManager')

    def __str__(self):
        return self.gig_title

    @staticmethod
    def get_gig_ids(ids):
        return Gig.objects.filter(id__in=ids)



class GigManager(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @staticmethod
    def get_gig(ids):
        return GigManager.objects.filter(id__in=ids)



class Order(models.Model):
    # Buyer
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120)
    package = models.ForeignKey(GigManager, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False, null=True)



    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.total = self.price
        super().save(*args, **kwargs)






































