from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
import ticketsales
import accounts
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
from django.contrib.auth.models import User
from .models import ProfileModel



def LoginView(request):

    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect(reverse(ticketsales.views.ConcertListView))


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        else:
            context = {
                'username': username,
                'errorMessage': 'کاربری با این مشخصات یافت نشد'
            }

            return render(request, 'accounts/login.html', context)

    else:

        return render(request, 'accounts/login.html', {})



def LogoutView(request):
    logout(request)

    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


@login_required
def ProfileView(request):
    profile = request.user.profile

    context = {
        "profile": profile,
    }

    return render(request, 'accounts/profile.html', context)



def ProfileRegisterView(request):

    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect(reverse(ticketsales.views.ConcertListView))


    if request.method == 'POST':
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)

        if profileRegisterForm.is_valid():
            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                                email=profileRegisterForm.cleaned_data['email'],
                                                password=profileRegisterForm.cleaned_data['password'],
                                            first_name=profileRegisterForm.cleaned_data['first_name'],
                                            last_name=profileRegisterForm.cleaned_data['last_name'])
            user.save()

            profileModel = ProfileModel(user=user, 
                                        profileimage=profileRegisterForm.cleaned_data['profileimage'],
                                        gender=profileRegisterForm.cleaned_data['gender'],
                                        credit=profileRegisterForm.cleaned_data['credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(accounts.views.LoginView))

    else:
        profileRegisterForm = ProfileRegisterForm()

    context = {
        "formData": profileRegisterForm,
    }

    return render(request, 'accounts/ProfileRegister.html', context)




def ProfileEditView(request):

    if request.method == 'POST':
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)

        if profileEditForm.is_valid() and userEditForm.is_valid():
            profileEditForm.save()
            userEditForm.save()

            return HttpResponseRedirect(reverse(accounts.views.ProfileView))



    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)



    context = {
        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
        "profileimage": request.user.profile.profileimage,
    }


    return render(request, 'accounts/profileEdit.html', context)




