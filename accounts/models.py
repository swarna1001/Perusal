from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from autoslug import AutoSlugField
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	city = models.CharField(max_length=30, blank=True)
	state = models.CharField(max_length=30, blank=True)

	slug = AutoSlugField(populate_from='user')
	bio = models.CharField(max_length=255, blank=True)
	friends = models.ManyToManyField("Profile", blank=True)

	genres = models.CharField(max_length=100, blank=True)

	

	def __str__(self):
		return f'{self.user.username}'

	def get_absolute_url(self):
		return "/accounts/{}".format(self.slug)


	# for image resize and save the updated profile in the database

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class FriendRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, 
		related_name='to_user', on_delete=models.CASCADE)
	
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, 
		related_name='from_user', on_delete=models.CASCADE)

	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)



class Genre(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='genres')
	
	has_autobiography = models.BooleanField(default=False, verbose_name="Autobiography")

	has_biography = models.BooleanField(default=False, verbose_name="Biography")

	has_drama = models.BooleanField(default=False, verbose_name="Drama")

	has_fairytale = models.BooleanField(default=False, verbose_name="Fairytale")

	has_fantasy = models.BooleanField(default=False, verbose_name="Fantasy")

	has_folktale = models.BooleanField(default=False, verbose_name="Folktale")

	has_historical_fiction = models.BooleanField(default=False, verbose_name="Historical Fiction")

	has_horror = models.BooleanField(default=False, verbose_name="Horror")

	has_informational = models.BooleanField(default=False, verbose_name="Informational")

	has_mystery = models.BooleanField(default=False, verbose_name="Mystery")

	has_myth = models.BooleanField(default=False, verbose_name="Myth")

	has_poetry = models.BooleanField(default=False, verbose_name="Poetry")

	has_realistic_fiction = models.BooleanField(default=False, verbose_name="Realistic Fiction")

	has_science_fiction = models.BooleanField(default=False, verbose_name="Science Fiction")


	def __str__(self):
		return " {}Genres ".format(self.user.username)


