# _*_ encoding:utf-8 _*_

from django import forms


# 验证表单内容
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
