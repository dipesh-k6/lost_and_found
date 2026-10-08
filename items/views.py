from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ItemForm,ItemImageForm

class FoundItemView(LoginRequiredMixin, View):

    def get(self, request):
        formitem = ItemForm()
        formimage = ItemImageForm()
        return render(request, "core/dashboard.html", {"submit_found_form": formitem, "image_form": formimage})
    

    def post(self, request):
        formitem = ItemForm(request.POST)
        formimage = ItemImageForm(request.POST,request.FILES)
        
        if formitem.is_valid() and formimage.is_valid():
            item_data = formitem.save(commit=False)
            item_data.user = request.user
            item_data.type = "found"

            image_data = formimage.save(commit=False)
            image_data.item = item_data

            item_data.save()
            image_data.save()
            # print("data saved")
            return redirect('dashboard_page')
        return render(request, "core/dashboard.html", {"submit_found_form": formitem, "image_form": formimage})

class LostItemView(LoginRequiredMixin, View):
    def get(self, request):
        formitem = ItemForm()
        formimage = ItemImageForm()
        return render(request, "core/dashboard.html", {"report_lost_form": formitem, "image_form": formimage})

    def post(self, request):
        formitem = ItemForm(request.POST)
        formimage = ItemImageForm(request.POST,request.FILES)
    
        if formitem.is_valid():
            item_data = formitem.save(commit=False)
            item_data.user = request.user
            item_data.type = "lost"

            if "image" in request.FILES:
                if formimage.is_valid():
                    image_data = formimage.save(commit=False)
                    image_data.item = item_data
                    item_data.save()
                    image_data.save()
                else:
                    return render(request, "core/dashboard.html", {"report_lost_form": formitem, "image_form": formimage})
            else:
                item_data.save()
            
            return redirect('dashboard_page')
        return render(request, "core/dashboard.html", {"report_lost_form": formitem, "image_form": formimage})