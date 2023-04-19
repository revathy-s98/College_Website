from django import forms

from collegewebsite.models import Member, Course


class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
                    # 'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        #           'lastname': forms.TextInput(attrs={'class': 'form-control'}),
                   'birthdate': forms.DateTimeInput(attrs={'class': 'form-control','type':'date'}),
                   'age': forms.NumberInput(attrs={'class': 'form-control'}),
        #            'gender': forms.RadioSelect(attrs={'class': 'form-control','type':'checkbox'}),
                   'phonenumber': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'department': forms.Select(attrs={'class': 'form-select'}),
                   'course': forms.Select(attrs={'class': 'form-select'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')