from django import forms
sexo=(
('Masculino',"M"),
('Femenino', "F"),
)

Tipo_Sangre = (
('O+', 'O+',),
('O-', 'O-'),
('A+', 'A+'),
('A-', 'A-'),
('B+', 'B+'),
('B-', 'B-'),
('AB+', 'AB+'),
('AB-', 'AB-'),
)
class Regvisitas(forms.Form):
    doctor = forms.CharField(max_length=100)
    motivo = forms.CharField()
    problema = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enfermedad o estado del paciente'}))
    NotaMedic = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Tratamientos que tiene que seguir el paciente.'}))

class RegPersonal(forms.Form):
    nombre = forms.CharField(max_length = 30)
    edad = forms.DecimalField(max_digits=100, decimal_places=2)
    fechaNacimiento = forms.CharField()
    Tipo_Sangre = forms.ChoiceField(choices=Tipo_Sangre)
    email = forms.EmailField()

class RegAlergias(forms.Form):
    medicamento = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'ejemplo: Paracetamol'}))
    motivo = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'ejemplo: dolor de cabeza'}))
    alergias = forms.CharField()
