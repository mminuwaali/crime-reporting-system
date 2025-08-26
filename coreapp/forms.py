from django import forms
from .models import Complaint, Response, Evidence

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'location', 'date_of_incident', 
                  'time_of_incident', 'category']
        widgets = {
            'date_of_incident': forms.DateInput(attrs={'type': 'date'}),
            'time_of_incident': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your response here...'}),
        }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['file', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Brief description of the evidence'}),
        }