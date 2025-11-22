from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from landing.models import LandingContent


class Command(BaseCommand):
    help = 'Configura o admin inicial para a Clima Ar Ne Refrigeração'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Nome de usuário do admin (padrão: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@Clima Ar Ne Refrigeração.com.br',
            help='E-mail do admin'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Senha do admin (padrão: admin123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        # Cria superusuário se não existir
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superusuário "{username}" criado com sucesso!')
            )
            self.stdout.write(f'📧 E-mail: {email}')
            self.stdout.write(f'🔑 Senha: {password}')
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Superusuário "{username}" já existe!')
            )

        # Cria registro inicial do LandingContent se não existir
        if not LandingContent.objects.exists():
            LandingContent.objects.create()
            self.stdout.write(
                self.style.SUCCESS('✅ Registro inicial do conteúdo da landing page criado!')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('✅ Registro do conteúdo da landing page já existe!')
            )

        self.stdout.write('\n' + '='*60)
        self.stdout.write('🎯 COMO EDITAR AS INFORMAÇÕES SOBRE A EMPRESA:')
        self.stdout.write('='*60)
        self.stdout.write('1. Acesse: http://127.0.0.1:8000/admin/')
        self.stdout.write(f'2. Faça login com: {username} / {password}')
        self.stdout.write('3. Clique em "Conteúdo da Landing Page"')
        self.stdout.write('4. Edite a seção "🏢 Seção Sobre a Empresa"')
        self.stdout.write('   - Sobre Título: Título da seção')
        self.stdout.write('   - Sobre Texto: História e descrição da empresa')
        self.stdout.write('   - Sobre Imagem: Foto da empresa/equipe')
        self.stdout.write('5. Clique em "Salvar" para aplicar as mudanças')
        self.stdout.write('='*60)