from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)#Turn the email to lowercase to avoid case sensitive or insensitive problems
        user = self.model(email=email, name=name)

        user.set_password(password)#Save password as harsh in case of database been hacked passwords will be seen as harsh
        user.save(using=self._db)#to specify ur database but we use _db so that u can use any kind of database

        return user


    def create_superuser(self,email,name,password):
        """Create and save a superuser """
        user = self.create_user(email,name,password)#we dont call self here because it has automaticaly pas in wen we call d func.

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects=UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of the user """
        return self.name

    def get_short_name(self):
        """Retrive short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
