from django.db import models

# Create your models here.

class Assessment(models.Model):

    # Fields
    target = models.ForeignKey(
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
        verbose_name = 'ideation star'
    )
    star2 = models.IntegerField(
        verbose_name = 'development star'
    )
    star3 = models.IntegerField(
        verbose_name = 'communication star'
    )
    star4 = models.IntegerField(
        verbose_name = 'overall star'
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
            self.target, 
            self.writter, 
            self.project, 
            self.star1, 
            self.star2, 
            self.star3, 
            self.star4, 
            self.text
        )