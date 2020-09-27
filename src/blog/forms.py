from django import forms 

from .models import BlogPost

class BlogPostForm(forms.Form):
    title   = forms.CharField()
    slug    = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea) 
    
    
    
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content'] #what you want to input
        
    
    def clean_title(self, *args, **kwagrs):
        title = self.cleaned_data.get('title')
        qs =BlogPost.objects.filter(title__iexact = title)##iexact를 쓰면 대문자 소문자 전부 같은걸로 취급.
        print(title)
        if qs.exists():
            raise forms.ValidationError("This title has already been used. please try another title name")
        return title