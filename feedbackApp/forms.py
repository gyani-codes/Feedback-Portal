from django import forms
from .models import Feedback, Course, Teacher
#TODO://
#Forms 1) forms.ModelForm padhana hai
class FeedbackForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ChoiceField(
            widget=forms.Select(attrs = {'class':'selectbox'}),
            choices=[
                (data , data) 
                for data in Course.objects.filter(semester=user.student.semester, department=user.student.department)]
        )   


        self.fields['skills'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
                ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )


        self.fields['knowledge'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
               ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )


        self.fields['interactivity'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
               ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )
        
    
    class Meta:
        model = Feedback
        fields = ('teacher_id','skills', 'knowledge', 'interactivity', 'review')
        widgets = {
            
            'course':forms.Select(attrs = {'class':'selectbox'}),
            'teacher_id':forms.Select(attrs = {'class':'selectbox'}),
            'review': forms.Textarea(attrs={'class':'form-control','rows':'3'}),


        }