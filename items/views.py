from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ItemForm, ItemImageForm
from .models import Item, ItemImage


class FoundItemView(LoginRequiredMixin, View):
    """logic to handle submitted found item"""

    def get(self, request):
        formitem = ItemForm()
        formimage = ItemImageForm()
        return render(
            request,
            "core/dashboard.html",
            {"submit_found_form": formitem, "image_form": formimage},
        )

    def post(self, request):
        formitem = ItemForm(request.POST)
        formimage = ItemImageForm(request.POST, request.FILES)

        if formitem.is_valid() and formimage.is_valid():
            item_data = formitem.save(commit=False)
            item_data.user = request.user
            item_data.type = "found"

            image_data = formimage.save(commit=False)
            image_data.item = item_data

            item_data.save()
            image_data.save()
            # print("data saved")
            return redirect("dashboard_page")
        return render(
            request,
            "core/dashboard.html",
            {"submit_found_form": formitem, "image_form": formimage},
        )


class LostItemView(LoginRequiredMixin, View):
    """logic to handle reported lost item"""

    def get(self, request):
        formitem = ItemForm()
        formimage = ItemImageForm()
        return render(
            request,
            "core/dashboard.html",
            {"report_lost_form": formitem, "image_form": formimage},
        )

    def post(self, request):
        formitem = ItemForm(request.POST)
        formimage = ItemImageForm(request.POST, request.FILES)

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
                    return render(
                        request,
                        "core/dashboard.html",
                        {"report_lost_form": formitem, "image_form": formimage},
                    )
            else:
                item_data.save()

            return redirect("dashboard_page")
        return render(
            request,
            "core/dashboard.html",
            {"report_lost_form": formitem, "image_form": formimage},
        )


class EditItem(LoginRequiredMixin, View):
    """logic to handle editing items and images"""

    def get(self, request, item_id):
        user_id = request.user.id
        item = Item.objects.get(user=user_id, id=item_id)

        if item:
            formitem = ItemForm(instance=item)

            try:
                item_image = ItemImage.objects.get(item=item.id)
                formimage = ItemImageForm(instance=item_image)
            except:
                formimage = ItemImageForm()

            return render(
                request,
                "core/dashboard.html",
                {"edit_item_form": formitem, "image_form": formimage, "item": item},
            )

        return redirect("dashboard_page")

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)

        # editing found items
        if item.type == "found":
            image = ItemImage.objects.get(item=item_id)
            formitem = ItemForm(request.POST, instance=item)
            formimage = ItemImageForm(request.POST, request.FILES, instance=image)

            if formitem.is_valid() and formimage.is_valid():
                item_data = formitem.save(commit=False)
                item_data.user = request.user

                image_data = formimage.save(commit=False)
                image_data.item = item_data

                item_data.save()
                image_data.save()

                return redirect("dashboard_page")

        # editing lost items
        else:
            formitem = ItemForm(request.POST, instance=item)
            formimage = ItemImageForm()

            if formitem.is_valid():
                item_data = formitem.save(commit=False)
                item_data.user = request.user

                if "image" in request.FILES:
                    image = ItemImage.objects.get(item=item_id)
                    formimage = ItemImageForm(
                        request.POST, request.FILES, instance=image
                    )

                    if formimage.is_valid():
                        image_data = formimage.save(commit=False)
                        image_data.item = item_data
                        item_data.save()
                        image_data.save()
                    else:
                        return render(
                            request,
                            "core/dashboard.html",
                            {
                                "edit_item_form": formitem,
                                "image_form": formimage,
                                "item": item,
                            },
                        )
                else:
                    item_data.save()

                return redirect("dashboard_page")

        return render(
            request,
            "core/dashboard.html",
            {"edit_item_form": formitem, "image_form": formimage, "item": item},
        )


class DeleteItem(LoginRequiredMixin, View):
    """logic to handle deleting items"""

    def get(self, request, item_id):
        verify_user = request.user
        item = Item.objects.get(id=item_id)

        if item.user.id == verify_user.id:
            item.delete()
            # return redirect("user_page")

        return redirect("dashboard_page")
