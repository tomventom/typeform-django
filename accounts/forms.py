from django import forms
from .models import Client
# from phonenumber_field.formfields import PhoneNumberField

class ClientCreationForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'full_name', 'company_name' , 'industry', 'position', 'city_headquarters', 'num_employees', 'phone_number')

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if not full_name:
            raise forms.ValidationError("Enter a full name")
        return full_name

    def clean_company_name(self):
        company_name = self.cleaned_data.get("company_name")
        if not company_name:
            raise forms.ValidationError("Enter a company name")
        return company_name

    def clean_industry(self):
        industry = self.cleaned_data.get("industry")
        if not industry:
            raise forms.ValidationError("Enter an industry")
        return industry

    def clean_position(self):
        position = self.cleaned_data.get("position")
        if not position:
            raise forms.ValidationError("Enter a position")
        return position

    def clean_city_headquarters(self):
        city_headquarters = self.cleaned_data.get("city_headquarters")
        if not city_headquarters:
            raise forms.ValidationError("Enter a city headquarters")
        return city_headquarters

    def clean_num_employees(self):
        num_employees = self.cleaned_data.get("num_employees")
        if not num_employees:
            raise forms.ValidationError("Enter number of employees")
        if num_employees <= 0:
            raise forms.ValidationError("Number of employees can not be negative.")
        return num_employees

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number:
            raise forms.ValidationError("Enter a phone number")
        return phone_number

    def save(self, commit=True):
        client = super(ClientCreationForm, self).save(commit=False)
        client.set_unusable_password()
        if commit:
            client.save()
        return client
