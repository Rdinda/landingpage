from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class LandingContent(models.Model):
    """Modelo singleton para conteúdo editável da landing page"""
    
    # Seção Hero
    hero_titulo = models.CharField(
        max_length=200, 
        default='Soluções Profissionais em Refrigeração',
        help_text='Título principal da seção hero'
    )
    hero_subtitulo = models.TextField(
        default='Especialistas em instalação, manutenção e reparo de sistemas de refrigeração comercial e industrial',
        help_text='Subtítulo explicativo da seção hero'
    )
    hero_cta_texto = models.CharField(
        max_length=50, 
        default='Solicitar Orçamento',
        help_text='Texto do botão principal'
    )
    hero_cta_link = models.CharField(
        max_length=200, 
        default='#contato',
        help_text='Link do botão principal'
    )
    hero_imagem = models.ImageField(
        upload_to='hero/', 
        blank=True, 
        null=True,
        help_text='Imagem de fundo da seção hero'
    )
    
    # Seção Sobre
    sobre_titulo = models.CharField(
        max_length=200, 
        default='Sobre a Clima Ar Ne Refrigeração',
        help_text='Título da seção sobre'
    )
    sobre_texto = models.TextField(
        default='Com mais de 10 anos de experiência no mercado de refrigeração, a Clima Ar Ne Refrigeração é especializada em soluções completas para sistemas de refrigeração comercial e industrial. Nossa equipe de técnicos certificados oferece serviços de instalação, manutenção preventiva e corretiva, garantindo máxima eficiência e durabilidade dos seus equipamentos.',
        help_text='Texto principal da seção sobre'
    )
    sobre_imagem = models.ImageField(
        upload_to='sobre/', 
        blank=True, 
        null=True,
        help_text='Imagem da seção sobre'
    )
    
    # Seção Contato
    contato_titulo = models.CharField(
        max_length=200, 
        default='Fale Conosco',
        help_text='Título da seção contato'
    )
    contato_descricao = models.TextField(
        blank=True,
        help_text='Descrição da seção contato'
    )
    
    # Informações de Contato
    telefone = models.CharField(
        max_length=20,
        default='(11) 99999-9999',
        help_text='Número de telefone principal'
    )
    whatsapp = models.CharField(
        max_length=20,
        default='5511999999999',
        help_text='Número do WhatsApp (formato: 5511999999999)'
    )
    whatsapp_boas_vindas = models.CharField(
        max_length=255,
        default='Olá! Gostaria de solicitar um orçamento para serviços de refrigeração.',
        help_text='Mensagem de boas-vindas usada ao abrir o WhatsApp via wa.me'
    )
    email = models.EmailField(
        default='contato@Clima Ar Ne Refrigeração.com.br',
        help_text='E-mail de contato principal'
    )
    endereco = models.CharField(
        max_length=200,
        default='São Paulo, SP',
        help_text='Endereço da empresa'
    )

    # Branding (logos configuráveis)
    logo_header = models.ImageField(
        upload_to='branding/',
        blank=True,
        null=True,
        help_text='Logo para o header (preferir versão com bom contraste em fundo azul escuro)'
    )
    logo_footer = models.ImageField(
        upload_to='branding/',
        blank=True,
        null=True,
        help_text='Logo para o footer (preferir versão clara ou monocromática, sem necessidade de inverter)'
    )
    
    # Redes sociais (opcionais)
    facebook_url = models.URLField(blank=True, null=True, help_text='URL da página no Facebook')
    instagram_url = models.URLField(blank=True, null=True, help_text='URL do perfil no Instagram')
    linkedin_url = models.URLField(blank=True, null=True, help_text='URL da página no LinkedIn')
    
    # Detalhes de Atendimento (editáveis)
    horario_semana = models.CharField(
        max_length=200,
        default='Segunda a Sexta: 8h às 18h',
        help_text='Horário de funcionamento em dias úteis'
    )
    horario_sabado = models.CharField(
        max_length=200,
        default='Sábado: 8h às 12h',
        help_text='Horário de funcionamento aos sábados'
    )
    horario_emergencias = models.CharField(
        max_length=200,
        default='Emergências: 24h',
        help_text='Horário de atendimento para emergências'
    )
    tempo_resposta_texto = models.CharField(
        max_length=200,
        default='Resposta em até 2 horas',
        help_text='Mensagem sobre tempo de resposta típico'
    )
    atendimento_emergencias_texto = models.CharField(
        max_length=200,
        default='Atendimento 24h para emergências',
        help_text='Mensagem destacando o atendimento de emergências'
    )
    area_atendimento_texto = models.CharField(
        max_length=200,
        default='Atendemos toda a Grande São Paulo',
        help_text='Área de cobertura/atendimento'
    )
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Conteúdo da Landing Page'
        verbose_name_plural = 'Conteúdo da Landing Page'
    
    def save(self, *args, **kwargs):
        self.pk = 1  # Força singleton
        super().save(*args, **kwargs)
    
    def __str__(self):
        return 'Conteúdo da Landing Page'


class TipoServico(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Tipo de Serviço'
        verbose_name_plural = 'Tipos de Serviço'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome


class Servico(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(
        max_length=100, 
        default='default-icon.svg',
        help_text='Nome do arquivo do ícone SVG'
    )
    imagem = models.ImageField(upload_to='servicos/', blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['ordem', 'titulo']
    
    def __str__(self):
        return self.titulo


class Depoimento(models.Model):
    nome_cliente = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200, blank=True)
    depoimento = models.TextField()
    foto = models.ImageField(upload_to='depoimentos/', blank=True, null=True)
    estrelas = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.nome_cliente} - {self.empresa}'


class MembroEquipe(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='equipe/', blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Membros da Equipe'
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return f'{self.nome} - {self.cargo}'


class Estatistica(models.Model):
    """Cards de estatísticas exibidos na landing (até 4 por conteúdo).

    Relacionado ao LandingContent para facilitar o gerenciamento via Admin.
    """
    landing_content = models.ForeignKey(
        LandingContent,
        on_delete=models.CASCADE,
        related_name='estatisticas'
    )
    titulo = models.CharField(max_length=100, help_text='Título do card (ex.: Clientes atendidos)')
    valor = models.CharField(max_length=50, help_text='Valor/quantidade (ex.: 150+, 10 anos)')
    descricao = models.CharField(max_length=200, blank=True, help_text='Descrição opcional abaixo do título')
    icone = models.CharField(
        max_length=100,
        blank=True,
        help_text='Nome do arquivo do ícone SVG (opcional)'
    )
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Estatística'
        verbose_name_plural = 'Estatísticas'
        ordering = ['ordem', 'titulo']

    def __str__(self):
        return f'{self.titulo} - {self.valor}'


class Lead(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    empresa = models.CharField(max_length=200, blank=True)
    tipo_servico = models.ForeignKey(
        TipoServico, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )
    mensagem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contatado = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.nome} - {self.email}'
