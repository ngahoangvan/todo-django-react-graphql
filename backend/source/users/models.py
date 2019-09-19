from __future__ import absolute_import
from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import SmartResize
from ..commons.cache import img_url_cache
import uuid
import os
import sys
# Create your models here.
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def get_unique_file_path(_, filename):
    """Get an unique file path with constant file upload prefix."""
    ext = filename.split('.')[1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(settings.FILE_UPLOAD_PREFIX_FOLDER_USER, filename)


class UserImage(models.Model):
    """User image models."""

    original = ProcessedImageField(upload_to=get_unique_file_path,
                                   format='JPEG',
                                   options={'quality': 100})
    medium = ImageSpecField(source='original',
                            processors=[SmartResize(100, 100)],
                            format='JPEG',
                            options={'quality': 100})
    small = ImageSpecField(source='original',
                           processors=[SmartResize(50, 50)],
                           format='JPEG',
                           options={'quality': 100})

    @img_url_cache(img_type='original')
    def get_original_url(self):
        """Get original image url."""
        try:
            return self.original.url
        except Exception:
            return ''

    @img_url_cache(img_type='medium')
    def get_medium_url(self):
        """Get medium image url."""
        try:
            return self.medium.url
        except Exception:
            return ''

    @img_url_cache(img_type='small')
    def get_small_url(self):
        """Get small image url."""
        try:
            return self.small.url
        except Exception:
            return ''


class UserProfile(models.Model):
    """User profile models."""

    class Meta:
        """User profile meta data."""

        ordering = ['user']

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='userprofile',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        UserImage,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)

    @property
    def full_name(self):
        """Custom full name method as a property."""
        return self.user.first_name + ' ' + self.user.last_name

    def __str__(self):
        """Default string."""
        return self.user.first_name + ' ' + self.user.last_name if self.user else ''
