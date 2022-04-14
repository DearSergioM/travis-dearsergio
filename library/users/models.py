# from django.db import models
# from django.contrib.auth.models import User

# class User(User):
#     # password = models.CharField(max_length = 256)

#     def Meta():
#         proxy = True
#         auto_created = True

#     # Overload del método string
#     def _str_(self):
#         return f'I am user {self.username}'