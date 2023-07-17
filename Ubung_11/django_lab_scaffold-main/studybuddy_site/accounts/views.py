from importlib.resources import Resource

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic


class ResourceEditForm:
    pass


class ResourceForm:
    pass


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    @login_required
    def edit(request, pk):
        resource = get_object_or_404(Resource, pk=pk)

        if request.method == 'POST':
            form = ResourceEditForm(request.POST, instance=resource)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('studybuddy_app:resource_detail', args=[pk]))
        else:
            form = ResourceEditForm(instance=resource)

        context = {
            "form": form,
            "http_method": 'POST',
            "action_url": reverse('studybuddy_app:resource_edit', args=[pk]),
            "button_text": 'Save',
        }
        return render(request, "studybuddy_app/resource_form.html", context)

    @login_required
    def edit(request, pk):
        resource = get_object_or_404(Resource, pk=pk)

        if request.method == 'POST':
            form = ResourceForm(request.POST, instance=resource)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("studybuddy_app:resource_detail", args=[resource.id]))
        else:
            form = ResourceForm(instance=resource)

        context = {
            "form": form,
        }
        return render(request, "studybuddy_app/resource_form.html", context)

    @login_required
    def edit(request, pk):
        resource = get_object_or_404(Resource, pk=pk)

        if request.method == 'POST':
            form = ResourceForm(request.POST, instance=resource)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("studybuddy_app:resource_detail", args=[resource.id]))
        else:
            form = ResourceForm(instance=resource)

        context = {
            "form": form,
        }
        return render(request, "studybuddy_app/resource_form.html", context)