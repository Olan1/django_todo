from django.db import models

# Create your models here.


# Item class inherrits from the Django models base class - Class Inherritance
class Item(models.Model):

    # Attributes
    name = models.CharField(max_length=50, null=False, blank=False)
    # Field can only have characters or text
    # blank=False makes the name field required on forms
    # null=False prevents items being created without a name programatically

    done = models.BooleanField(null=False, blank=False, default=False)
    # Can be either True or False
    # Default is False to stop items being marked True by accident

    # Override the Django models base class's default name for the
    # objects created (Items in this instance)
    def __str__(self):
        # return the Item class name attribute
        return self.name
