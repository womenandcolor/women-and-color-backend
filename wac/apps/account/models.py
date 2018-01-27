from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     """
#     Extends from the user model
#     """
#     user = models.OneToOneField(
#         User
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def display_name(self):
#         return u"%s %s".strip() % (self.user.first_name, self.user.last_name)

#     def __str__(self):
#         return self.display_name()

#     def __unicode__(self):
#         return self.display_name()
