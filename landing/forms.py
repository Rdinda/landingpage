from django import forms
from .models import Lead, TipoServico, LandingContent
import urllib.parse


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['nome', 'email', 'telefone', 'empresa', 'tipo_servico', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'seu@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': '(11) 99999-9999'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Nome da sua empresa'
            }),
            'tipo_servico': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Descreva suas necessidades de refrigeração...',
                'rows': 4
            }),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'empresa': 'Empresa',
            'tipo_servico': 'Tipo de Serviço',
            'mensagem': 'Mensagem',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_servico'].queryset = TipoServico.objects.filter(ativo=True)
        self.fields['tipo_servico'].empty_label = "Selecione o tipo de serviço"
        
        # Campos obrigatórios
        for field_name in ['nome', 'email', 'telefone', 'tipo_servico']:
            self.fields[field_name].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower().strip()
        return email

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            # Remove caracteres não numéricos
            telefone = ''.join(filter(str.isdigit, telefone))
            if len(telefone) < 10:
                raise forms.ValidationError('Telefone deve ter pelo menos 10 dígitos.')
        return telefone


class LandingContentForm(forms.ModelForm):
    """
    Form do Admin para LandingContent, permitindo multi-linhas
    para o campo whatsapp_boas_vindas sem mudar o schema (sem migração).
    """
    class Meta:
        model = LandingContent
        fields = "__all__"
        widgets = {
            "whatsapp_boas_vindas": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_whatsapp_boas_vindas(self):
        msg = self.cleaned_data.get("whatsapp_boas_vindas", "")
        if msg is None:
            return msg

        # Normaliza espaços e remove espaços em branco nas bordas
        normalized = msg.strip()

        # Validação preventiva do tamanho da mensagem codificada na URL
        # Mantemos um limite conservador para evitar URLs excessivamente longas.
        encoded = urllib.parse.quote(normalized, safe="")
        MAX_ENCODED_LEN = 2000  # limite conservador para o parâmetro text
        if len(encoded) > MAX_ENCODED_LEN:
            raise forms.ValidationError(
                (
                    "Mensagem muito longa para ser enviada via URL do WhatsApp. "
                    f"Tamanho codificado: {len(encoded)} (limite: {MAX_ENCODED_LEN}). "
                    "Reduza o texto ou o número de quebras de linha."
                )
            )

        return normalized

    class Media:
        js = [
            'js/admin-whatsapp-counter.js',
        ]