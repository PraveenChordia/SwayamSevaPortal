from django import forms
from SwayamSeva.models import Documents
from SwayamSeva.models import CompleteUserDetails

requirements = {
    'MNREGA': ('Uid', 'Ration_no', 'Mobile_no', 'Bank_Acc_no', 'IFSC_Code',
               'MICR_Code', 'Bank', 'Branch'),
    'PMJDY': ('Uid', 'Mobile_no',),
    'SSA': ('Uid', 'Mobile_no',),
    'APY': ('Uid', 'Voter_id', 'Mobile_no', 'Bank_Acc_no', 'IFSC_Code',
            'Uid', 'MICR_Code', 'Bank', 'Branch'),
    'BY': ('Uid', 'Voter_id', 'Ration_no', 'Pan_no', 'Electricity_bill', 'Mobile_no',
           'Bank_Acc_no', 'IFSC_Code', 'MICR_Code', 'Bank', 'Branch'),
    'PDS': ('Uid', 'BPL_no', 'Mobile_no')
}


class defForm(forms.Form):
    Name = forms.CharField(max_length=150, disabled=True)
    Aadhaar = forms.CharField(max_length=12, disabled=True)


class docMGNREGA(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['MNREGA']

    def clean(self):
        if self.is_valid():
            mobile = self.cleaned_data['Mobile_no']
            if len(mobile) != 10:
                raise forms.ValidationError('Please enter a 10 digit Mobile No.')


class docPMJDY(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['PMJDY']

    def clean_Mobile_no(self):
        mobile = self.cleaned_data['Mobile_no']
        if len(mobile) != 10:
            raise forms.ValidationError("Please enter a 10 digit Mobile Number")
        return mobile


class docSSA(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['SSA']

    def clean(self):
        if self.is_valid():
            mobile = self.cleaned_data['Mobile_no']
            if len(mobile) != 10:
                raise forms.ValidationError('Please enter a 10 digit Mobile No.')


class docAPY(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['APY']

    def clean(self):
        if self.is_valid():
            mobile = self.cleaned_data['Mobile_no']
            if len(mobile) != 10:
                raise forms.ValidationError('Please enter a 10 digit Mobile No.')


class docBY(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['BY']

    def clean(self):
        if self.is_valid():
            mobile = self.cleaned_data['Mobile_no']
            if len(mobile) != 10:
                raise forms.ValidationError('Please enter a 10 digit Mobile No.')


class docPDS(forms.ModelForm):
    Uid = forms.ModelChoiceField(queryset=CompleteUserDetails.objects.all(), widget=forms.HiddenInput, disabled=True,
                                 label='')

    class Meta:
        model = Documents
        fields = requirements['PDS']

    def clean(self):
        if self.is_valid():
            mobile = self.cleaned_data['Mobile_no']
            if len(mobile) != 10:
                raise forms.ValidationError('Please enter a 10 digit Mobile No.')
