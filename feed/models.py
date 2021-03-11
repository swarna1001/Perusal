from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image


class Post(models.Model):
	text_post = models.TextField()
	post_image = models.ImageField(blank=True, upload_to = 'post_images')

	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)


	def __str__(self):
		return "{} - {}".format(self.text_post, self.user_name)


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


	# for image resize and save the updated profile in the database

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.post_image.path)

		if img.height > 600 or img.width > 600:
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.post_image.path)







class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.TextField()
	comment_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)



	
	

