from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Assessment(models.Model):
    # Fields

    a_id = models.AutoField(
        primary_key = True
    )
    
    subject = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment'
    )

    writter = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment'
    )

    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment'
    )


    star1 = models.IntegerField(
        verbose_name = 'ideation star',
        validators = [rangeValidation] 
    )
    star2 = models.IntegerField(
        verbose_name = 'development star',
        validators = [rangeValidation] 
    )
    star3 = models.IntegerField(
        verbose_name = 'communication star',
        validators = [rangeValidation] 
    )
    star4 = models.IntegerField(
        verbose_name = 'overall star',
        validators = [rangeValidation] 
    )

    text = models.TextField(
        verbose_name = 'assessment text',
        max_length = 100
        )

    # Metadata
    class Meta: 
        verbose_name = 'assessment'

    # Methods
    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n" .format(
            self.subject, 
            self.writter, 
            self.project, 
            self.star1, 
            self.star2, 
            self.star3, 
            self.star4, 
            self.text
        )

    def rangeValidation(self, value):
        if not value in [1, 2, 3, 4, 5]:
            raise ValidationError("not a valid value")
        else :
            return value


