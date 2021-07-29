from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=210)
    
    def __str__(self):
        return self.title
    

class Gig(models.Model):
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