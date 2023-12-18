from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.urls import reverse

from .forms import CarouselForm, SlideForm
from .models import Carousel, Slide


# Create your views here.


def index_display(request):
    context = {}
    context["form"] = CarouselForm()
    context["object_list"] = Carousel.objects.all()
    return render(request, "display_board/index_display.html", context)


def display(request, pk):
    context = {}
    context["carousel"] = Carousel.objects.get(key=pk)
    return render(request, "display_board/display.html", context)


def create_display(request):
    context = {}
    form = CarouselForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            carousel = form.save()
            response = HttpResponse()
            response["HX-Redirect"] = reverse(
                "display_board:edit_display", kwargs={"pk": carousel.key}
            )
            return response

    context["form"] = form
    return render(request, "display_board/create_display.html", context)


def delete_display(request, pk):
    context = {}
    obj = get_object_or_404(Carousel, key=pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def edit_display(request, pk):
    context = {}
    carousel = Carousel.objects.get(key=pk)
    context["carousel"] = carousel
    return render(request, "display_board/edit_display.html", context)


def slide_create(request, pk):
    context = {}
    carousel = get_object_or_404(Carousel, key=pk)
    print(request.POST)
    form = SlideForm(request.POST or None)
    print(request.method)
    if request.method == "POST":
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.parent = carousel
            print(form.instance.image)
            form.save()
            # print(slide.image)
            return redirect("display_board:slide_detail", pk=form.instance.key)
            # return render(request, 'display_board/slide_contact.html', context)
    print("end2")
    context["form"] = form
    context["carousel_id"] = pk
    return render(request, "display_board/slide_form.html", context)


def slide_detail(request, pk):
    context = {}
    obj = get_object_or_404(Slide, key=pk)
    context["slide"] = obj

    return render(request, "display_board/slide_detail.html", context)


def slide_edit(request, pk):
    context = {}
    obj = get_object_or_404(Slide, key=pk)
    form = SlideForm(request.POST or None, instance=obj)
    print(request.POST)
    if request.method == "POST":
        print(request.FILES)
        form = SlideForm(request.POST, request.FILES, instance=obj)
        # save the data from the form and redirect to detail_view
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("display_board:slide_detail", pk=obj.key)

    context["form"] = form
    return render(request, "display_board/slide_edit.html", context)


def slide_delete(request, pk):
    context = {}
    obj = get_object_or_404(Slide, key=pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
