from django.db import models

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d71dbfc (Initialise for Heroku)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
<<<<<<< HEAD
=======
# Create your models here.
>>>>>>> 06eb41d (Initial Commit)
=======
>>>>>>> d71dbfc (Initialise for Heroku)
