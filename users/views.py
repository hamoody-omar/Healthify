from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('user_profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')

    else:

        try:
            Profile.objects.get(
                user__username=request.user.username)
        except:
            user_profile = Profile()
            user_profile.user = request.user
            user_profile.save()

        u_form = UserUpdateForm(instance=request.user)

        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def make_appointment(request):
    if request.POST:
        return redirect('user_profile')

    else:
        context = {}
        providers = ['Novant Health', 'Med Assist',
                     'Care Ring', 'Physicians Reachout']
        availability = ['Available', 'Unavailable',
                        'Unavailable', 'Unavailable', ]

        context['appointment'] = zip(providers, availability)
        return render(request, 'users/make_appointment.html', context)


def view_med_his(request):

    return render(request, 'users/user_view_med_his.html', {})


def get_coverage(request):
    return redirect('user_profile')
    return render(request, 'users/get_coverage.html')


def user_view_appointments(request):
    appointments = ['Care Ring at 26/03/2019 06:28',
                    'Novant Health at 14/06/2019 11:34']
    return render(request, 'users/user_view_appointments.html', {'appointments': appointments})


def about(request):
    return redirect('user_profile')
    return render(request, 'users/about.html', {'title': 'About'})
