from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import BirthdayForm
from .models import Birthday


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    # template_name = 'birthday/birthday_confirm_delete.html' # можно не указывать т.к имя шаблона подходит
    ...


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    ...


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    ...
