from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
#from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import  AuthenticationForm 
from django.views.generic import View
from django.views.generic import CreateView,FormView

from .forms import StudentSignUpForm,TeacherSignUpForm,ContactForm
from .models import Student,Teacher


class StudentSignUp(CreateView):
    model = Student
    form_class = StudentSignUpForm
    template_name = 'accounts/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
class TeacherSignUp(CreateView):
    model = Teacher
    form_class = TeacherSignUpForm
    template_name = 'accounts/teacher_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



      
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    success_url = "/"
