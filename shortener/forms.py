from django import forms
from .validators import validate_dot_com,validate_url
class SubmitURLForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url,validate_dot_com])


    # def clean(self):
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     print(cleaned_data)
    #     # url = cleaned_data.get("url")
    #     url = cleaned_data.get('url')
    #     # print(url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     print(url)
    #     return url
    # #     return url
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     # url_validator = URLValidator()
    #     # try:
    #         # url_validator(url)
    #     # except:
    #     #     raise forms.ValidationError("Invalid URL for this field")
    #     # print(url)
    #     # return url
    #     if not "com" in url:
    #         raise forms.ValidationError("This is not valid of no .com")
    #     return url
