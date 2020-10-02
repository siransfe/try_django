from django import forms 

from .models import BlogPost

class BlogPostForm(forms.Form):
    title   = forms.CharField()
    slug    = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea) 
    
    
    
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date'] #what you want to input
        
    def clean_title(self, *args, **kwagrs):
        
        instance = self.instance
        #print(instance) # blogpost object 임
        title = self.cleaned_data.get('title')
        qs =BlogPost.objects.filter(title__iexact = title)##iexact를 쓰면 대문자 소문자 구분 
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        if qs.exists(): 
            raise forms.ValidationError("This title has already been used. please try another title name")
        return title
    
    