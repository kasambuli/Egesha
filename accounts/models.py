from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from driver.models import
# from lotOwner.models import
# from lotManager.models import


class DriverProfile(models.Model):
    '''
    Profile model class
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, related_name='driver_profile', on_delete=models.CASCADE, null=False, db_index=True)
    phone_number = models.DecimalField(max_digits=30, decimal_places=0, null=True)
    license = models.CharField(max_length=10, null=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(
            "edit_profile",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["join_date"]

    '''
    Class methods:
    update_profile:
    find_profile: allows us to search for a user using their profile name.
    get_profile_by_id: allows us to get profile by id.
    '''
    @classmethod
    def update_profile(cls, id, bio):
        update = cls.objects.filter(id=id).update(bio=bio)
        return update

    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles


class OwnerProfile(models.Model):
    '''
    Profile model class
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, related_name='owner_profile', on_delete=models.CASCADE, null=False, db_index=True)
    phone_number = models.DecimalField(max_digits=30, decimal_places=0, null=True)
    national_id = models.CharField(max_length=30, null=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(
            "edit_profile",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["join_date"]


class ManagerProfile(models.Model):
    '''
    Profile model class
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, related_name='manager_profile', on_delete=models.CASCADE, null=False, db_index=True)
    phone_number = models.DecimalField(max_digits=30, decimal_places=0, null=True)
    national_id = models.CharField(max_length=30, null=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(
            "edit_profile",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["join_date"]
