
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.core.paginator import Paginator
from socialmedia.forms import SocialmediaForm
from socialmedia.models import Socialmedia
from .models import Post
from .forms import PostForm


# @login_requried(login_url="/login")
def photo_create(request):  # i am server -> this is request
    # if not request.user.is_staff or not request.user.is_authenticated:
    # raise Http404
    if not request.user.is_authenticated:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Your photo has been added.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "photo_form.html", context)  # this is my response


def photo_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    initial_data = {
        # "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    form = SocialmediaForm(
        request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")  # accesing data
        content_data = form.cleaned_data.get("content")
        new_comment, created = Socialmedia.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data
        )

    comments = Socialmedia.objects.filter_by_instance(instance)
    context = {
        "title": instance.title,
        "photo": instance.photo,
        "instance": instance,
        "comments": comments,
        "socialmedia_form": form,
    }
    return render(request, "photo_detail.html", context)


def photo_files(request):
    queryset = Post.objects.all().order_by("-time")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(title__contains=query)
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "object_file": queryset,
        "title": "Photos",
        "page_obj": page_obj,

    }
    return render(request, "photo_files.html",  context)


def photo_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Your photo has been updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "photo_form.html", context)


def photo_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Your photo has been deleted.")
    return redirect("photo_files")
