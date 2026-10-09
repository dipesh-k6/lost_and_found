from django.shortcuts import redirect

def user_only(func):
    def views_func(request, *args, **kwargs):
        if not request.user.is_staff:
           return func(request, *args, **kwargs)
        else:
            return redirect('dashboard_page')

    return views_func