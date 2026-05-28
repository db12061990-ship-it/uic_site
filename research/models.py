from django.db import models


class ResearchWork(models.Model):
    employee = models.CharField(max_length=200)
    title = models.TextField()
    deadline = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    result = models.CharField(max_length=200)

    pdf_file = models.FileField(
        upload_to='research_pdfs/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.employee


# Create your models here.
