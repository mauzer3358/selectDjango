from django import forms
from .models import DirectorModel

class DirectorForm(forms.ModelForm):
    class Meta:
        model = DirectorModel
        fields = '__all__'

class VyborForm(forms.Form):
    price_max = forms.DecimalField(max_digits=10, decimal_places=3, label='Максимальный бюджет')
    opyt = forms.IntegerField(label='Опыт')
    search_genre = forms.CharField(max_length=50, label='Выбор жанра')
