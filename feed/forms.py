from django import forms
from .models import Comment, Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['text_post', 'image_post', 'tags']

class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
		

