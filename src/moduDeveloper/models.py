from django.db import models
from .validators import validate_file_size

#Reference: https://wayhome25.github.io/django/2017/03/20/django-ep5-model/


# Create your models here.
class Developer(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    u_ID = models.AutoField(
        verbose_name='user ID',
        name='uID',
        primary_key=True,
        unique = True,
    )

    profile_image_path = models.ImageField(
        verbose_name='upload profile image',
        name='profile image',
        upload_to= 'uploads/user_{0}'.format(u_ID),
        validators=[validate_file_size],
    )

    portfolio = models.TextField(
        verbose_name='portfolio text',
        name='porfolio text',
        max_length=5000,
        blank=True,
    )

    #Developer-Propose-Project
    proposed_projects = models.ForeignKey(
        'moduProject.Project',
        on_delete=models.CASCADE,
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Follow-Many Developer
    follow = models.ManyToManyField(
        "self",
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Member of-Many Project
    member_of = models.ManyToManyField(
        'moduProject.Project',
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Invite-Many Project
    #unique relationship
    invite = models.ManyToManyField(
        'moduProject.Project',
        related_name='developers',
        related_query_name='developer'
    )

    #Many Developer-Favorite-Many Project
    favorite = models.ManyToManyField(
        'moduProject.Project',
        related_name='developers',
        related_query_name='developer'
    )

    
    # Metadata
    class Meta:
        verbose_name = 'developer'
        ordering = ['u_ID']

    # Methods
    def __str__(self):
        """String for representing the Developer object in Developer Page."""
        return "{}\n{}\n{}\n{}\n{}\n{}\n" .format(
            self.profile_image_path, 
            self.portfolio,
            self.proposed_projects,
            self.follow,
            self.favorite,
            self.invite)
