from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(DeleteView):
    # template_name = 'birthday/birthday_confirm_delete.html'
    # # можно не указывать т.к имя шаблона подходит
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(CreateView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayUpdateView(UpdateView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["birthday_countdown"] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context
