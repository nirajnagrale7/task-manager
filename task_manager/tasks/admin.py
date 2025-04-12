# tasks/admin.py

from django.contrib import admin
from django import forms
from django.db.models import Q
from .models import Task

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Pop the request from kwargs
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if self.request and not self.request.user.is_superuser:
            # Limit assigned_by to only the logged-in user
            self.fields['assigned_by'].queryset = self.fields['assigned_by'].queryset.filter(id=self.request.user.id)
            self.fields['assigned_by'].initial = self.request.user
            self.fields['assigned_by'].disabled = True

            # Exclude self from assigned_to
            self.fields['assigned_to'].queryset = self.fields['assigned_to'].queryset.exclude(id=self.request.user.id)
            
class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm

    def get_form(self, request, obj=None, **kwargs):
        # Inject request into the form
        AdminForm = super().get_form(request, obj, **kwargs)

        class AdminFormWithRequest(AdminForm):
            def __new__(cls, *args, **kwargs_):
                kwargs_['request'] = request
                return AdminForm(*args, **kwargs_)

        return AdminFormWithRequest

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(assigned_to=request.user) | Q(assigned_by=request.user))

admin.site.register(Task, TaskAdmin)
