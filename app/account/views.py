from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from django.conf import settings

from account.forms import UserAccountRegistrationForm, UserAccountProfileForm, ContactUs


class CreateUserAccountView(CreateView):
    model = settings.AUTH_USER_MODEL
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        messages.success(self.request, "New user has been successfully created!")
        return reverse('account:profile')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as a user'}
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        messages.success(self.request, "You've just successfully logged in")
        return reverse('account:profile')


class UserAccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout from LMS'}
    login_url = reverse_lazy('account:login')


class UserAccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = UserAccountProfileForm
    login_url = reverse_lazy('account:login')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')


class ContactUsView(FormView):
    template_name = 'contact_us.html'
    extra_context = {'title': 'Send us a message'}
    success_url = reverse_lazy('index')
    form_class = ContactUs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
