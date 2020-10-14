# forms.py

from django import forms
from .models import *


class Add_Article_Form(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title',
                  'author',
                  'date',
                  'image',
                  'content',
                  'description',
                  'url'
        ]


## As of now I'm not using this form, but am keeping just in case.
class Subscriber_Form(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['name',
                  'email'
        ]
        exclude = ['subscriber_id']
