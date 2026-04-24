from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Q
from datetime import date
from .models import jobappli,Profile
from .forms import jobappliform,ProfileForm
from google import genai
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Create your views here.
def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("dashboard")
    return render(request,'register.html',{"form":form})
def log_out(request):
    logout(request)
    return redirect("loginn")
def loginn(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
            
    return render(request,'loginn.html')

@login_required
def dashboard(request):
    applications= jobappli.objects.filter(user=request.user)
    count=applications.count()
    stcount=applications.values("status").annotate(count=Count("status"))
    stdata={"Applied":0,"Interview":0,"Offer":0,"Rejected":0}
    for item in stcount:
        stdata[item["status"]] = item["count"]
    context = {
        "total": count,
        "status_data": stdata,
    }

    return render(request, "dashboard.html", context)

@login_required
def applist(request):
    applis=jobappli.objects.filter(user=request.user).order_by("-created_at")
    query=request.GET.get('q','')
    status = request.GET.get('status', '')

    if query:
        applis = applis.filter(
            Q(comname__icontains=query) |
            Q(title__icontains=query)
        )
    if status:
        applis = applis.filter(status=status)

    return render(request, "applist.html", {"applis": applis, "query": query, "status": status, "today":date.today()})
    
@login_required
def addappli(request):
    if request.method=="POST":
        form=jobappliform(request.POST)
        if form.is_valid():
            app=form.save(commit=False)
            app.user=request.user
            app.save()
            return redirect("applist")
    else:
        form = jobappliform()
    return render(request,"addappli.html",{"form":form})
@login_required
def editappli(request,id):
    app = jobappli.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = jobappliform(request.POST, instance=app)

        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            return redirect("applist")

    else:
        form = jobappliform(instance=app)

    return render(request, "editappli.html", {"form": form})
    
@login_required
def delappli(request,id):
    app=jobappli.objects.get(id=id, user=request.user)
    if request.method=="POST":
        app.delete()
    return redirect("applist")
@login_required
def coverletter(request):
    cover_letter = ""
    
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect("profile")  # force user to fill profile first
    
    if request.method == "POST":
        job_description = request.POST.get("job_description", "")

        prompt = f"""
        Write a professional cover letter for the following job description:
        {job_description}

        Candidate Name: {user_profile.full_name}
        Candidate Skills: {user_profile.skills}
        Candidate Bio: {user_profile.bio}

        Make it formal, concise and compelling. 3 paragraphs max.
        """
        client = genai.Client(api_key=os.getenv("AIzaSyDQC3rOu1zTj1PkzBeG0f345KE_qh0h_Y8"))
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        cover_letter = response.text

       

    return render(request, "coverletter.html", {
        "cover_letter": cover_letter,
        "profile": user_profile
    })

@login_required
def profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect("coverletter")
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, "profile.html", {"form": form})
    