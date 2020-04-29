import jwt  

from datetime import datetime, timedelta  

from django.conf import settings  
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class
    """

    def create_user(self, email, password=None):
        """Create and return a `User` with an email and password."""

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token`
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JWT that stores this user's email and has an expiry
        date set to 1 day into the future.
        """

        dt = datetime.now() + timedelta(days=1)
        data = {
            'email': self.email,
            'exp': int(dt.strftime('%s'))
        }
        token = jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
