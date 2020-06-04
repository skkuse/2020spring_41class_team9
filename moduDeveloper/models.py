from django.db import models

#Reference: https://wayhome25.github.io/django/2017/03/20/django-ep5-model/


# Create your models here.
class Developer(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    uID = models.CharField(
        primary_key=True,
        max_length=20,
    )

    profile_image = models.FileField(
        verbose_name='profile image',
        upload_to="developer/profile_pic", #not sure
    )

    portfolio = models.TextField(
        verbose_name='portfolio text',
        max_length=5000,
        blank=True,
    )

    #Developer-Propose-Project
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='developers',
        related_query_name='developer'
    )

    #Developer-Write-Assessment
    write_assessment = models.ForeignKey(
        'Assessment',
        on_delete=models.CASCADE,
        related_name='developers',
        related_query_name='developer'
    )

    #Developer-Receive-Assessment
    receive_assessment = models.ForeignKey(
        'Assessment',
        on_delete=models.CASCADE,
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Follow-Many Developer
    follow = models.ManyToManyField(
        'Developer',
        related_name='developers'
        ,related_query_name='developer'
    )

    #Many Developer-Member of-Many Project
    member_of = models.ManyToManyField(
        'Project',
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Invite-Many Project
    invite = models.ManyToManyField(
        'Project',
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Favorite-Many Project
    favorite = models.ManyToManyField(
        'Project',
        related_name='developers',
        related_query_name='developer'
    )

    
    # Metadata
    class Meta:
        verbose_name = 'developer'
        ordering = ['uID']

    # Methods
    def __str__(self):
        """String for representing the Developer object in Developer Page."""
        return self.portfolio
