from django.shortcuts import render


def landing(request):
    return render(
        request,
        'start_pages/landing.html',
    )


def idea_manage(request):
    return render(
        request,
        'start_pages/idea_manage.html',
    )