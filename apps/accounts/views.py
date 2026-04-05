from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from base.emails import send_verification_email
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# View for user registration
def register_view(request):
    if request.method == "POST":
        # Extract user data from the submitted form
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Check if the username already exists in the database
        user_obj = User.objects.filter(username=username)
        if user_obj.exists():
            messages.error(request, "Username already exists...")
            return redirect('register')
        
        # Create a new user but keep them inactive until email verification
        user_obj = User.objects.create_user(username=username, email=email, password=password)
        user_obj.is_active = False
        user_obj.save()
        
        # Send a verification email to the new user
        send_verification_email(user_obj)
        messages.success(request, "Pls check your email to verify your account...")
        return redirect('register')
    
    # Renders the registration form for GET requests
    return render(request, 'accounts/register.html')

# View to process email verification link
def verify_email(request, user_id):
    # Fetch the user using the ID provided in the URL
    user_obj = User.objects.get(id=user_id)
    # Activate the user's account
    user_obj.is_active = True
    user_obj.save()
    
    # Update the profile to mark email as verified
    profile = Profile.objects.get(user=user_obj)
    profile.is_email_verified = True
    profile.save()
    
    messages.success(request, "Account verified successfully...")
    # Redirect the user to the login page
    return redirect('login')

# View for user login
def login_view(request):
    if request.method == "POST":
        # Extract login credentials from the form
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate the user against the database
        user = authenticate(username=username, password=password)

        # If authentication fails, redirect back to login
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('login')

        # Retrieve the user's profile and ensure it exists
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            messages.error(request, "Profile not found")
            return redirect('login')

        # Ensure the user has verified their email before allowing login
        if not profile.is_email_verified:
            messages.error(request, "Email is not verified")
            return redirect('login')

        # Log the user into the session
        login(request, user)
        messages.success(request, "Logged in successfully")
        
        # Redirect to the 'next' URL if present, otherwise to the home page
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('home')
        
    # Renders the login page for GET requests
    return render(request, 'accounts/login.html')

# View to log out the current user
def logout_view(request):
    # Terminates the user's session
    logout(request)
    # Redirects the user back to the home page
    return redirect('home')
