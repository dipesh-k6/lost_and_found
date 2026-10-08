from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from items.models import Item,ItemImage

def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def user_page(request, username, userid):
    verify_username = request.user.username
    verify_userid = request.user.id

    if username == verify_username and userid == verify_userid:
        user_items = Item.objects.filter(user=verify_userid)
        return render(request, 'core/dashboard.html', {"user_verified":True, "user_items":user_items})
    else:
        return redirect('dashboard_page')
