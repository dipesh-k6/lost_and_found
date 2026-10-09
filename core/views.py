from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from items.models import Item
from .auth import user_only

def dashboard(request):
    found_items = Item.objects.filter(type="found", status="active").prefetch_related("images").order_by("-date")
    lost_items = Item.objects.filter(type="lost", status="active").prefetch_related("images").order_by("-date")

    return render(request, 'core/dashboard.html', {"found_items":found_items, "lost_items":lost_items})

@user_only
@login_required
def user_page(request, username, userid):
    verify_username = request.user.username
    verify_userid = request.user.id

    if username == verify_username and userid == verify_userid:
        user_items = Item.objects.filter(user=verify_userid)
        return render(request, 'core/dashboard.html', {"user_verified":True, "user_items":user_items})
    else:
        return redirect('dashboard_page')
