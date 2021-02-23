from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, Genres_choices
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, FriendRequest

# add Post model to the feed app

from feed.models import Post

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
import random

User = get_user_model()

# Create your views here.

def signup_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = form.save()

			# log the user in
			login(request, user)
			# user is directed to his homepage, after successful login
			# return redirect('home:homepage')

			# user is directed to login page after the successful registration
			return redirect('accounts:login')


	else:
		form = RegisterForm()
	
	return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():

			#log in the user
			user = form.get_user()
			login(request, user)

			return redirect('accounts:my_profile')
	else:
		form = AuthenticationForm()

	return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)

		# temporary logout direct
		# might create a different logout view

		#return redirect('basic_home/')
		return render(request, 'accounts/logout.html')


@login_required
def my_profile_view(request):

	users = Profile.objects.exclude(user = request.user)
	sent_friend_requests = FriendRequest.objects.filter(from_user = request.user)
	sent_to = []
	friends = []
	for user in users:
		friend = user.friends.all()	
		for f in friend:
			if f in friends:
				friend = friend.exclude(user = f.user)

		friends += friend

	my_friends = request.user.profile.friends.all()
	for i in my_friends:
		if i in friends:
			friends.remove(i)

	if request.user.profile in friends:
		friends.remove(request.user.profile)

	random_list = random.sample(list(users), min(len(list(users)), 10))

	for r in random_list:
		if r in friends:
			random_list.remove(r)

	friends += random_list

	for i in my_friends:
		if i in friends:
			friends.remove(i)

	for sent in sent_friend_requests:
		sent_to.append(sent.to_user)

	context = {
			'users' : friends,
			'sent' : sent_to
	}

	
	return render(request, 'accounts/my_profile.html', context)


# still working
def genres_view(request):
	if request.method == "POST":
		form = Genres_choices(request.POST)

		if form.is_valid():
			user = form.save()

			# log the user in
			#login(request, user)
			# user is directed to his homepage, after successful login
			# return redirect('home:homepage')

			# user is directed to login page after the successful registration
			return redirect('accounts:my_profile')


	else:
		form = Genres_choices()
	
	return render(request, 'accounts/genres.html', {'form':form})



@login_required
def edit_profile_view(request):
    # return HttpResponse(slug)
    if request.method == "POST":

    	u_form = UserUpdateForm(request.POST, instance=request.user)
    	p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


    	if u_form.is_valid() and p_form.is_valid():
    		u_form.save()
    		p_form.save()

    		messages.success(request, f'your profile has been updated!')
    		return redirect('accounts:my_profile')

    	else:
    		messages.success(request, f'Fill all the fields!')

    else:

	    u_form = UserUpdateForm(instance=request.user)
	    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    	'u_form' : u_form,
    	'p_form' : p_form,
    }

    return render(request, 'accounts/homepage.html', context)

#-------------------------------------------------------------------------
# recent changes (after stable version)


# users_list view used in the my_profile view

@login_required
def users_list(request):
	
	users = Profile.objects.exclude(user = request.user)
	sent_friend_requests = FriendRequest.objects.filter(from_user = request.user)
	sent_to = []
	friends = []
	for user in users:
		friend = user.friends.all()	
		for f in friend:
			if f in friends:
				friend = friend.exclude(user = f.user)

		friends += friend

	my_friends = request.user.profile.friends.all()
	for i in my_friends:
		if i in friends:
			friends.remove(i)

	if request.user.profile in friends:
		friends.remove(request.user.profile)

	random_list = random.sample(list(users), min(len(list(users)), 10))

	for r in random_list:
		if r in friends:
			random_list.remove(r)

	friends += random_list

	for i in my_friends:
		if i in friends:
			friends.remove(i)

	for sent in sent_friend_requests:
		sent_to.append(sent.to_user)

	context = {
			'users' : friends,
			'sent' : sent_to
	}

	return render(request, "accounts/users_list.html", context)

# any user's profile view

@login_required
def profile_view(request, slug):

	p = Profile.objects.filter(slug=slug).first()
	u = p.user
	sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
	rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
	#user_posts = Post.objects.filter(user_name=u)

	friends = p.friends.all()

	# is this user our friend
	button_status = 'none'
	if p not in request.user.profile.friends.all():
		button_status = 'not_friend'

		# if we have sent him a friend request
		if len(FriendRequest.objects.filter(
			from_user=request.user).filter(to_user=p.user)) == 1:
				button_status = 'friend_request_sent'

		# if we have recieved a friend request
		if len(FriendRequest.objects.filter(
			from_user=p.user).filter(to_user=request.user)) == 1:
				button_status = 'friend_request_received'

	context = {
		'u': u,
		'button_status': button_status,
		'friends_list': friends,
		'sent_friend_requests': sent_friend_requests,
		'rec_friend_requests': rec_friend_requests,
		#'post_count': user_posts.count
	}

	return render(request, "accounts/profile.html", context)







def friend_list(request):
	p = request.user.profile
	friends = p.friends.all()
	context = { 
		'friends' : friends
	}
	return render (request, "accounts/friend_list.html", context)


@login_required
def send_friend_request(request, id):
	user = get_object_or_404 (User, id = id)
	frequest , created = FriendRequest.objects.get_or_create(
						from_user = request.user,
						to_user = user )

	return HttpResponseRedirect('/accounts/{}'.format(user.profile.slug))

@login_required
def cancel_friend_request(request, id):
	user = get_object_or_404(User, id = id)
	frequest = FriendRequest.objects.filter(
				from_user = request.user,
				to_user = user).first()

	frequest.delete()
	return HttpResponseRedirect('/accounts/{}'.format(user.profile.slug))


@login_required
def accept_friend_request(request, id):
	from_user = get_object_or_404(User, id = id)
	frequest = FriendRequest.objects.filter(from_user = from_user, to_user = request.user).first()
	user_1 = frequest.to_user
	user_2 = from_user

	user_1.profile.friends.add(user_2.profile)
	user_2.profile.friends.add(user_1.profile)

	if(FriendRequest.objects.filter(from_user = request.user, to_user = from_user).first()):
		request_received = FriendRequest.objects.filter(from_user = request.user, 
			to_user = from_user).first()

		request_received.delete()

	frequest.delete()
	return HttpResponseRedirect('/accounts/{}'.format(request.user.profile.slug))


@login_required
def delete_friend_request(request, id):
	from_user = get_object_or_404(User, id)
	frequest = FriendRequest.objects.filter(from_user = from_user, to_user = request.user).first()
	frequest.delete()
	return HttpResponseRedirect('/accounts/{}'.format(request.user.profile.slug))


def delete_friend(request, id):
	user_profile = request.user.profile
	friend_profile = get_object_or_404(Profile, id = id)
	user_profile.friends.remove(friend_profile)
	friend_profile.friends.remove(user_profile)

	return HttpResponseRedirect('/accounts/{}'.format(friend_profile.slug))



# renders the logged in user's profile

@login_required
def my_profile(request):
	p = request.user.profile
	you = p.user
	sent_friend_requests = FriendRequest.objects.filter(from_user = you)
	rec_friend_requests = FriendRequest.objects.filter(to_user = you)

	user_posts = Post.objects.filter(user_name = you)
	friends = p.friends.all()

