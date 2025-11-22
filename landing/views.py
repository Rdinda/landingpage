from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.conf import settings
from .models import LandingContent, Servico, Depoimento, MembroEquipe, Estatistica
from .forms import ContatoForm


class LandingPageView(TemplateView):
    template_name = 'landing/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Conteúdo editável da landing page
        try:
            landing_content = LandingContent.objects.first()
        except LandingContent.DoesNotExist:
            landing_content = None
        
        # Serviços ativos ordenados
        servicos = Servico.objects.filter(ativo=True).order_by('ordem')
        
        # Depoimentos ativos
        depoimentos = Depoimento.objects.filter(ativo=True).order_by('-created_at')[:6]
        
        # Membros da equipe ativos
        equipe = MembroEquipe.objects.filter(ativo=True).order_by('ordem')

        # Estatísticas (até 4 cards) vinculadas ao conteúdo
        if landing_content:
            estatisticas = Estatistica.objects.filter(
                landing_content=landing_content,
                ativo=True
            ).order_by('ordem')[:4]
        else:
            estatisticas = []
        
        # Formulário de contato
        form = ContatoForm()
        
        context.update({
            'landing_content': landing_content,
            'servicos': servicos,
            'depoimentos': depoimentos,
            'equipe': equipe,
            'estatisticas': estatisticas,
            'form': form,
            'DEBUG': settings.DEBUG,
        })
        
        return context


@require_http_methods(["POST"])
def contato_submit(request):
    """
    View para processar o formulário de contato via AJAX
    """
    form = ContatoForm(request.POST)
    
    if form.is_valid():
        lead = form.save()
        
        # Resposta de sucesso
        return JsonResponse({
            'success': True,
            'message': 'Obrigado! Recebemos sua mensagem e entraremos em contato em breve.'
        })
    else:
        # Resposta com erros
        return JsonResponse({
            'success': False,
            'errors': form.errors,
            'message': 'Por favor, corrija os erros no formulário.'
        })


def contato_success(request):
    """
    Página de sucesso após envio do formulário (fallback para não-AJAX)
    """
    return render(request, 'landing/contato_success.html')


# View alternativa para formulário sem AJAX
def contato_form_view(request):
    """
    View para processar formulário de contato sem AJAX (fallback)
    """
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obrigado! Recebemos sua mensagem e entraremos em contato em breve.')
            return redirect('contato_success')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ContatoForm()
    
    return render(request, 'landing/contato_form.html', {'form': form})
