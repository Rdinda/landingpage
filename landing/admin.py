from django.contrib import admin
from django.utils.html import format_html
from .models import LandingContent, Servico, Lead, TipoServico, Depoimento, MembroEquipe, Estatistica
from .forms import LandingContentForm


@admin.register(LandingContent)
class LandingContentAdmin(admin.ModelAdmin):
    form = LandingContentForm
    inlines = []
    fieldsets = (
        ('🎯 Seção Hero (Topo da Página)', {
            'fields': ('hero_titulo', 'hero_subtitulo', 'hero_cta_texto', 'hero_cta_link', 'hero_imagem'),
            'description': '🎨 Configure o conteúdo da seção principal (hero) da landing page - primeira impressão dos visitantes',
            'classes': ('wide',)
        }),
        ('🏢 Seção Sobre a Empresa', {
            'fields': ('sobre_titulo', 'sobre_texto', 'sobre_imagem'),
            'description': '📝 Configure o conteúdo da seção sobre a empresa - história, missão e valores da Clima Ar Ne Refrigeração',
            'classes': ('wide',)
        }),
        ('📞 Seção Contato', {
            'fields': ('contato_titulo', 'contato_descricao'),
            'description': '💬 Configure o conteúdo da seção de contato - formulário e chamadas para ação',
            'classes': ('wide',)
        }),
        ('📱 Informações de Contato', {
            'fields': ('telefone', 'whatsapp', 'whatsapp_boas_vindas', 'email', 'endereco'),
            'description': '🌐 Configure as informações de contato da empresa (telefone, WhatsApp, e-mail e endereço) - aparecem no footer e botão flutuante',
            'classes': ('wide',)
        }),
        ('🕒 Detalhes de Atendimento', {
            'fields': (
                'horario_semana',
                'horario_sabado',
                'horario_emergencias',
                'tempo_resposta_texto',
                'atendimento_emergencias_texto',
                'area_atendimento_texto',
            ),
            'description': 'Defina os horários de funcionamento e mensagens auxiliares exibidas na seção de contato (tempo de resposta, atendimento de emergências e área de atendimento).',
            'classes': ('wide',)
        }),
        ('🎨 Branding', {
            'fields': ('logo_header', 'logo_footer'),
            'description': 'Defina os logos para o header e footer. Utilize versões com bom contraste para cada fundo.',
            'classes': ('wide',)
        }),
        ('🔗 Redes sociais', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url'),
            'description': 'Defina os links das redes sociais (opcionais). Ícones só serão exibidos no site quando houver link configurado.',
            'classes': ('wide',)
        }),
    )
    
    list_display = ('__str__', 'updated_at')
    readonly_fields = ('updated_at',)
    
    def has_add_permission(self, request):
        # Permite apenas uma instância (singleton)
        return not LandingContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Não permite deletar o conteúdo
        return False
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Adiciona help text mais detalhado para o campo sobre_texto
        if 'sobre_texto' in form.base_fields:
            form.base_fields['sobre_texto'].help_text = (
                "Descreva a história da empresa, experiência no mercado, "
                "diferenciais competitivos e valores. Use parágrafos para organizar o conteúdo."
            )
        # Adiciona help text para o campo de mensagem do WhatsApp
        if 'whatsapp_boas_vindas' in form.base_fields:
            form.base_fields['whatsapp_boas_vindas'].help_text = (
                "Mensagem padrão enviada ao abrir o WhatsApp. Aceita múltiplas linhas; "
                "quebras de linha serão convertidas para %0A na URL. Limite de 2000 caracteres codificados (URL). "
                "Observação: o campo no banco aceita até 255 caracteres em texto bruto."
            )
        return form


@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
    list_editable = ('ativo',)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem', 'ativo', 'created_at')
    list_filter = ('ativo', 'created_at')
    search_fields = ('titulo', 'descricao')
    list_editable = ('ordem', 'ativo')
    ordering = ('ordem',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'ordem', 'ativo')
        }),
        ('Mídia', {
            'fields': ('icone', 'imagem'),
            'description': 'Configure o ícone e imagem do serviço'
        }),
    )


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'empresa', 'estrelas', 'ativo', 'created_at')
    list_filter = ('ativo', 'estrelas', 'created_at')
    search_fields = ('nome_cliente', 'empresa', 'depoimento')
    list_editable = ('ativo',)
    ordering = ('-created_at',)


@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ordem', 'ativo', 'created_at')
    list_filter = ('ativo', 'created_at')
    search_fields = ('nome', 'cargo')
    list_editable = ('ordem', 'ativo')
    ordering = ('ordem',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'tipo_servico', 'created_at', 'contatado')
    list_filter = ('contatado', 'tipo_servico', 'created_at')
    search_fields = ('nome', 'email', 'empresa')
    list_editable = ('contatado',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informações do Lead', {
            'fields': ('nome', 'email', 'telefone', 'empresa')
        }),
        ('Solicitação', {
            'fields': ('tipo_servico', 'mensagem')
        }),
        ('Gestão', {
            'fields': ('contatado', 'observacoes', 'created_at')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('tipo_servico')


# Customização do Admin Site
admin.site.site_header = 'Clima Ar Ne Refrigeração - Administração'
admin.site.site_title = 'Clima Ar Ne Refrigeração Admin'
admin.site.index_title = 'Painel de Controle da Landing Page'

# Inline para Estatísticas (cards)
class EstatisticaInline(admin.TabularInline):
    model = Estatistica
    extra = 0
    max_num = 4
    fields = ('titulo', 'valor', 'descricao', 'icone', 'ordem', 'ativo')
    ordering = ('ordem',)

# Anexa inline às LandingContentAdmin
LandingContentAdmin.inlines = [EstatisticaInline]
