# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from Home.models import Imagepage
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ImageUploadForm,
)  # Import the form we just created
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def home(request):
    images = Imagepage.objects.all()[:4]
    return render(request, "home.html", {"image": images})


class MyLoginView(LoginView):
    redirect_authenticated_user = False
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("profile")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Signout Successful.")
    # Redirect to a success page.
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save user to Database
            username = form.cleaned_data.get(
                "username"
            )  # Get the username that is submitted
            messages.success(
                request, f"Account created for {username}!"
            )  # Show sucess message when account is created
            return redirect(home)
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.add_message(
                request, messages.SUCCESS, f"Your account has been updated!"
            )
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {"u_form": u_form}
    return render(request, "profile.html", context)


@login_required
def imageupload(request):
    if request.method == "POST":
        i_form = ImageUploadForm(request.POST, request.FILES)
        if i_form.is_valid():
            i_form.instance.user_name = request.user.username
            i_form.save()
            messages.add_message(
                request, messages.SUCCESS, f"Your image has been uploaded!"
            )
            return redirect("profile")
    else:
        i_form = ImageUploadForm()
    context = {"i_form": i_form}
    return render(request, "profile.html", context)


@login_required
def profile_with_forms(request):
    u_form = UserUpdateForm(instance=request.user)
    i_form = ImageUploadForm()
    images = Imagepage.objects.filter(user_name=request.user)

    context = {
        "u_form": u_form,
        "i_form": i_form,
        "image": images,
    }
    return render(request, "profile.html", context)


def delete_image_view(request, image_id):
    image = Imagepage.objects.get(pk=image_id)
    image.img.delete(save=False)
    image.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
