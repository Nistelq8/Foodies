from django.shortcuts import render, redirect
from .forms import  UserRegister, UserLogin, Create_Recipe
from django.contrib.auth import login, authenticate, logout


def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("homepage")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)




def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("homepage")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("success-page")


def create_recipy_view(request):
    form = Create_Recipe
    context = {
        "form": form,
    }
    return render(request, 'homepage.html', context)

# def create_category_view(request):
#     form = Create_Category
#     context = {
#         "form": form,
#     }
#     return render(request, '', context)


# def create_ingredient_view(request):
#     form = Create_Ingredient
#     context = {
#         "form": form,
#     }
#     return render(request, '', context)