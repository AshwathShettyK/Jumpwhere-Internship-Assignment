from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from .forms import ShortenUrlForm
from .models import ShortenedUrl


def home_view(request):
    form = ShortenUrlForm(request.POST or None)
    shortened = None
    latest_urls = ShortenedUrl.objects.all()[:5]

    if request.method == "POST" and form.is_valid():
        long_url = form.cleaned_data["long_url"]
        shortened, created = ShortenedUrl.objects.get_or_create(long_url=long_url)
        if not created:
            shortened = ShortenedUrl.objects.get(long_url=long_url)
        return redirect("shortener:result", short_code=shortened.short_code)

    return render(request, "shortener/index.html", {"form": form, "latest_urls": latest_urls})


def result_view(request, short_code):
    shortened = get_object_or_404(ShortenedUrl, short_code=short_code)
    return render(request, "shortener/result.html", {"shortened": shortened})


def redirect_view(request, short_code):
    shortened = get_object_or_404(ShortenedUrl, short_code=short_code)
    shortened.click_count += 1
    shortened.save(update_fields=["click_count"])
    return redirect(shortened.long_url)
