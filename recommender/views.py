from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "total_users": get_user_model().objects.count(),
        "total_predictions": Prediction.objects.count(),
    }
    return render(request, "home.html", context)


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not name or not email or not contact or not password:
            messages.error(request,"Please fill all required fields.")
            return redirect("signup")
        if len(password) <6 :
            messages.error(request,"Password should be atleast 6 characters.")
            return redirect("signup")
        if User.objects.filter(username=email):
            messages.error(request,"Account already exists.")
            return redirect("signup")
        user=User.objects.create_user(username=email,password=password)
        if " " in name:
            first,last= name.split(" ",1)
        else:
            first,last= name, ""
        user.first_name,user.last_name =first, last
        user.save()

        UserProfile.objects.create(user=user,contact=contact)
        login(request,user)
        messages.success(request,"Account created succesfully.")
        return redirect("predict")
    return render(request,'signup.html')


from .ml.loader import predict_one, load_bundle
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required
def predict_view(request):
    feature_order = load_bundle()["features"]
    result = None
    last_data = None

    if request.method == "POST":
        data = {}

        try:
            for c in feature_order:
                data[c] = float(request.POST.get(c))
        except ValueError:
            messages.error(request, "Please enter valid numeric values.")
            return redirect("predict")

        label = predict_one(data)

        Prediction.objects.create(
            user=request.user,
            **data,
            predicted_label=label
        )

        messages.success(request, f"Recommended Crop: {label}")

        return redirect("predict")  

    return render(request, "predict.html", {
        "feature_order": feature_order,
        "result": result,
        "last_data": last_data
    })
def logout_view(request):
    logout(request)
    messages.success(request,"Logout succesfully!")
    return redirect("login")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if not user:
            messages.error(request,"Invalid login credentials")
            return redirect("login")
        login(request,user)
        messages.success(request,"Logged in succesfully.")
        return redirect("predict")
    return render(request,'login.html')


@login_required
def user_history_view(request):
    predictions= Prediction.objects.filter(user=request.user)
    return render(request,'history.html',locals())

from django.shortcuts import get_object_or_404
@login_required
def user_delete_prediction(request,id):
    prediction=get_object_or_404(Prediction,id=id,user=request.user)
    predictions= Prediction.objects.filter(user=request.user)
    prediction.delete()
    messages.success(request,"Entry removed !!")
    return redirect("user_history")

@login_required
def profile_view(request):
    profile =UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        name=request.POST.get("name")
        contact = request.POST.get("contact")
        if name:
            parts = name.split(" ",1)
            request.user.first_name = parts[0]
            request.user.last_name = parts[1] if len(parts) > 1 else ""
        profile.contact = contact
        request.user.save()
        profile.save()
        messages.success(request,"Profile Updated")
    return render(request,'profile.html',locals())

@login_required
def change_password_view(request):
   
    if request.method == "POST":
        current=request.POST.get("current_password")
        new = request.POST.get("new")
        confirm = request.POST.get("confirm_password")
        if not request.user.check_password(current):
            messages.error(request,"Current Password is incorrect.")
            return redirect("change_password")
        if len(new) < 6:
            messages.error(request,"New Password is must me at least 6 characters.")
            return redirect("change_password")
        if new != confirm:
            messages.error(request,"Passwords do not match.")
            return redirect("change_password")
        request.user.set_password(new)
        request.user.save()
        user=authenticate(request,username=request.user.username,password=new)
        if user:
            
             login(request,user)
             messages.success(request,"Password changed succesfully.")
             return redirect("change_password")
    return render(request,'change_password.html',locals())

def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request,"Invalid login credentials")
            return redirect("admin_login")

        if not user.is_staff:
            messages.error(request,"You are not authorised for this.")
            return redirect("admin_login")

        login(request,user)
        messages.success(request,"Logged in succesfully.")
        return redirect("admin_dashboard")

    return render(request,'admin_login.html')


def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff,login_url='admin_login')
def admin_dashboard_view(request):
    
    return render(request,'admin_dashboard.html',locals())


