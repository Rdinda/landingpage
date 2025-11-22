from django.core.management.base import BaseCommand
from landing.models import LandingContent, TipoServico, Servico, Depoimento, MembroEquipe


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais para a Clima Ar Ne Refrigeração'

    def handle(self, *args, **options):
        self.stdout.write('Populando dados iniciais...')

        # Criar conteúdo da landing page
        landing_content, created = LandingContent.objects.get_or_create(
            defaults={
                'hero_titulo': 'Refrigeração Profissional de Excelência',
                'hero_subtitulo': 'Soluções completas em climatização e refrigeração para empresas e indústrias. Qualidade garantida há mais de 15 anos.',
                'hero_cta_texto': 'Solicitar Orçamento Gratuito',
                'hero_cta_link': '#contato',
                'sobre_titulo': 'Sobre a Clima Ar Ne Refrigeração',
                'sobre_texto': '''Com mais de 15 anos de experiência no mercado de refrigeração, a Clima Ar Ne Refrigeração se consolidou como referência em soluções profissionais de climatização.

Nossa equipe altamente qualificada oferece serviços completos, desde a instalação até a manutenção de sistemas de refrigeração para empresas de todos os portes.

Trabalhamos com as melhores marcas do mercado e garantimos qualidade, eficiência e durabilidade em todos os nossos projetos.''',
                'contato_titulo': 'Entre em Contato',
                'contato_descricao': 'Solicite um orçamento gratuito e sem compromisso. Nossa equipe está pronta para atender suas necessidades.',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Conteúdo da landing page criado'))
        else:
            self.stdout.write('• Conteúdo da landing page já existe')

        # Criar tipos de serviço
        tipos_servico = [
            {'nome': 'Instalação', 'slug': 'instalacao'},
            {'nome': 'Manutenção Preventiva', 'slug': 'manutencao-preventiva'},
            {'nome': 'Manutenção Corretiva', 'slug': 'manutencao-corretiva'},
            {'nome': 'Reparo de Equipamentos', 'slug': 'reparo-equipamentos'},
            {'nome': 'Consultoria Técnica', 'slug': 'consultoria-tecnica'},
            {'nome': 'Projeto Personalizado', 'slug': 'projeto-personalizado'},
        ]

        for tipo_data in tipos_servico:
            tipo, created = TipoServico.objects.get_or_create(
                slug=tipo_data['slug'],
                defaults=tipo_data
            )
            if created:
                self.stdout.write(f'✓ Tipo de serviço criado: {tipo.nome}')

        # Criar serviços
        servicos = [
            {
                'titulo': 'Instalação de Ar Condicionado',
                'descricao': 'Instalação profissional de sistemas de ar condicionado residencial, comercial e industrial com garantia de qualidade e eficiência energética.',
                'ordem': 1,
            },
            {
                'titulo': 'Manutenção Preventiva',
                'descricao': 'Manutenção programada para garantir o funcionamento perfeito dos seus equipamentos, aumentando a vida útil e reduzindo custos.',
                'ordem': 2,
            },
            {
                'titulo': 'Reparo e Assistência Técnica',
                'descricao': 'Reparo rápido e eficiente de equipamentos de refrigeração com peças originais e técnicos especializados.',
                'ordem': 3,
            },
            {
                'titulo': 'Refrigeração Industrial',
                'descricao': 'Soluções completas para refrigeração industrial, incluindo câmaras frias, sistemas de resfriamento e climatização de grandes ambientes.',
                'ordem': 4,
            },
            {
                'titulo': 'Consultoria Técnica',
                'descricao': 'Análise técnica especializada para otimização de sistemas existentes e projetos de novos sistemas de refrigeração.',
                'ordem': 5,
            },
            {
                'titulo': 'Atendimento 24h',
                'descricao': 'Suporte emergencial 24 horas para situações críticas que exigem intervenção imediata em seus sistemas de refrigeração.',
                'ordem': 6,
            },
        ]

        for servico_data in servicos:
            servico, created = Servico.objects.get_or_create(
                titulo=servico_data['titulo'],
                defaults=servico_data
            )
            if created:
                self.stdout.write(f'✓ Serviço criado: {servico.titulo}')

        # Criar depoimentos
        depoimentos = [
            {
                'nome_cliente': 'Carlos Silva',
                'empresa': 'Restaurante Sabor & Arte',
                'depoimento': 'Excelente serviço! A Clima Ar Ne Refrigeração instalou nosso sistema de refrigeração e desde então não tivemos nenhum problema. Equipe muito profissional.',
                'estrelas': 5,
            },
            {
                'nome_cliente': 'Maria Santos',
                'empresa': 'Supermercado Central',
                'depoimento': 'Trabalho com a Clima Ar Ne Refrigeração há 3 anos. Sempre pontuais, eficientes e com preços justos. Recomendo para qualquer empresa.',
                'estrelas': 5,
            },
            {
                'nome_cliente': 'João Oliveira',
                'empresa': 'Indústria Alimentícia JO',
                'depoimento': 'A manutenção preventiva da Clima Ar Ne Refrigeração evitou muitos problemas em nossa linha de produção. Investimento que vale a pena.',
                'estrelas': 4,
            },
        ]

        for depoimento_data in depoimentos:
            depoimento, created = Depoimento.objects.get_or_create(
                nome_cliente=depoimento_data['nome_cliente'],
                empresa=depoimento_data['empresa'],
                defaults=depoimento_data
            )
            if created:
                self.stdout.write(f'✓ Depoimento criado: {depoimento.nome_cliente}')

        # Criar membros da equipe
        equipe = [
            {
                'nome': 'Roberto Silva',
                'cargo': 'Diretor Técnico',
                'bio': 'Engenheiro com mais de 20 anos de experiência em refrigeração industrial.',
                'ordem': 1,
            },
            {
                'nome': 'Ana Costa',
                'cargo': 'Coordenadora de Projetos',
                'bio': 'Especialista em projetos de climatização para grandes empresas.',
                'ordem': 2,
            },
            {
                'nome': 'Pedro Santos',
                'cargo': 'Técnico Sênior',
                'bio': 'Técnico especializado em manutenção e reparo de equipamentos.',
                'ordem': 3,
            },
        ]

        for membro_data in equipe:
            membro, created = MembroEquipe.objects.get_or_create(
                nome=membro_data['nome'],
                defaults=membro_data
            )
            if created:
                self.stdout.write(f'✓ Membro da equipe criado: {membro.nome}')

        self.stdout.write(
            self.style.SUCCESS('\n🎉 Dados iniciais populados com sucesso!')
        )
        self.stdout.write(
            self.style.WARNING('\n📝 Acesse o admin em /admin/ para editar o conteúdo:')
        )
        self.stdout.write('   Usuário: admin')
        self.stdout.write('   Senha: admin123')