from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


from profiles_api import models
from profiles_api.models import ProfileFeedItem







class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self, email, name, password=None,):
        """create a new user proffile"""
        if not email:
            raise ValueError('user must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with givin details"""
        user = self.create_user(email=email, name=name, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


    




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model ffor users in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieves the full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieves the short name of user"""
        return self.name
    
    def __str__(self):
        """Returns a string representation of user"""
        return self.email
    


class ProfilefeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return tthe model as a string"""
        return self.status_text


