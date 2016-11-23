from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.views import View
from app.models import Task, Status


def index(request):
    context = { "tasks": Task.objects.all() }
    return render(request, "index.html", context)


def delete(request, id):
    t = Task.objects.get(id=id)
    t.delete()
    # return reverse("index_view")
    return HttpResponseRedirect(reverse('index'))


class TaskView(View):
    template_name = 'task.html'
    # model = Task

    def get(self, request, id):
        if id:
            t = Task.objects.get(id=id)
        else:
            t = Task()
        context = {"task": t,
                   "statuses": Status.objects.all()}
        return render(request, self.template_name, context)

    def post(self, request, id):
        if id:
            t = Task(id=id)
            t.task = request.POST['task']
            t.status_id = request.POST['status']
            t.save()
        else:
            t = Task.objects.create(task=request.POST['task'],
                                status_id=request.POST['status'])
        return HttpResponseRedirect(reverse('index'))
        return render(request, self.template_name, {"task": t})



class StatusView(View):
    template_name = 'status.html'
    model = Status

    def get(self, request, id):
        if id:
            s = Status.objects.get(id=id)
        else:
            s = Status()
        return render(request, self.template_name, {"status": s})

    def post(self, request, id):

        s = Status.objects.create(status=request.POST['status'])
        return render(request, self.template_name, {"status": s})
