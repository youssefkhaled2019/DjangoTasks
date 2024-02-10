from typing import Any
from django import forms
from .models import post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields["text"].label = ""
            # self.fields["password"].label = ""
            
    class Meta:
        model=post
        fields=["text"]
        widgets={
                    'text':forms.Textarea(attrs={"rows":"4", "cols":"50","placeholder":"..."}),
                
                }