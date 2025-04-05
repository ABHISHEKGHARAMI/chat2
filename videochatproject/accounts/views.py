from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import  UserUpdateForm , ProfileUpdateForm
from .models import Profile

# Create your views here.

# first view for the profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        #  check is the forms are valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile of {request.user.username} is updated ...')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request,
                  'accounts/profile.html',
                  {
                      'u_form' : u_form,
                      'p_form' : p_form
                  })



# for the contacts of the user
@login_required
def contacts(request):
    user = User.objects.exclude(user=request.user)
    return render(
        request,
        'accounts/contacts.html',
        {
            'user' : user
        }
    )