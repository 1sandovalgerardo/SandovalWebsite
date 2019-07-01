# -*- coding: utf-8 -*-

from django import forms
from AppBlog.models import PostModel,CommentModel


class PostForm(forms.ModelForm):

    class Meta():
        model = PostModel
        fields = ('author', 'title', 'text')
        # widget to grab a particular field
        widgets = {'title': forms.TextInput(attrs={'class': 'textinput'}),
                   'text': forms.Textarea(attrs={'class': 'editable\
                                                 medium-editor-textarea\
                                                 postcontent'})}


class CommentForm(forms.ModelForm):

    class Meta():
        model = CommentModel
        fields = ('author', 'text')
        widgets = {'author': forms.TextInput(attrs={'class': 'textinput'}),
                   'text': forms.Textarea(attrs={'class': 'editable\
                                                 medium-editor-textares'})}



