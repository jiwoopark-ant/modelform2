from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    
    #어울리는 폼 자동생성 코드
   
    class Meta:
        model=Article
        fields='__all__'