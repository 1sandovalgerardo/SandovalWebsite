# -*- coding: utf-8 -*-
from django import forms
from AppToDo.models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]