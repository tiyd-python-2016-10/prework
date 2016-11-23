from django.shortcuts import render
from app.models import DTwit


def index_view(request):
    if request.POST:
        m = DTwit(message=request.POST['message'])
        m.save()
    messages = DTwit.objects.all()
    context = { "messages": messages }
    return render(request, "index.html", context)
