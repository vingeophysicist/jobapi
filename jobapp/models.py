from django.db import models

# Create your models 


class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.company_name



