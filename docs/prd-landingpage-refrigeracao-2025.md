# Clima Ar Ne Refrigeração: Plataforma Digital de Refrigeração Profissional (Versão Landing Page)

## Product Overview

### Problema
Em um mercado de refrigeração comercial e industrial em crescimento, profissionais e empresas enfrentam dificuldades para encontrar serviços especializados, orçamentos rápidos e informações confiáveis sobre manutenção e instalação de sistemas de refrigeração. A falta de uma plataforma centralizada resulta em perda de tempo, ineficiências e oportunidades perdidas para leads qualificados.

### Público-Alvo
- Proprietários de negócios (supermercados, restaurantes, indústrias).
- Gerentes de manutenção predial.
- Profissionais autônomos de refrigeração buscando parcerias.
- Empresas de refrigeração em busca de visibilidade.

### Proposta de Valor
Clima Ar Ne Refrigeração oferece uma landing page intuitiva e otimizada que centraliza informações sobre serviços de refrigeração profissional, facilitando o contato rápido e a geração de leads. Com foco em conversão, a plataforma transforma visitantes em clientes potenciais através de chamadas claras para ação (CTAs) e conteúdo persuasivo.

### Objetivo de Mercado
Capturar 15% do mercado local de refrigeração em 12 meses, gerando pelo menos 50 leads qualificados mensais através da landing page única.

## Core Features

A landing page única é dividida em seções integradas para uma experiência fluida de navegação via scroll ou âncoras.

### Funções do Usuário
- **Visitante Anônimo**: Navega pelas seções, visualiza informações e envia formulários de contato.
- **Administrador**: Gerencia leads e conteúdo via painel Django admin (não visível na landing page).

### Módulos de Funcionalidades
- **Seção Home (Hero)**: Banner principal com chamada para ação, destacando benefícios e CTA para contato.
- **Seção Serviços**: Descrição detalhada de serviços oferecidos, com cards interativos e depoimentos.
- **Seção Contato**: Formulário de orçamento com campos validados e integração para envio de e-mails.
- **Seção Sobre**: Informações sobre a empresa, equipe e valores, com elementos visuais para credibilidade.

## Core Process

### Fluxo do Visitante
1. Acesso à landing page única.
2. Scroll pelas seções: Home → Serviços → Sobre → Contato.
3. Interação com CTAs em cada seção para direcionamento ao formulário de contato.
4. Envio de formulário e confirmação via e-mail.

### Fluxo de Lead Magnet
1. Visitante preenche formulário na seção Contato.
2. Sistema Django processa e armazena lead.
3. E-mail automático de confirmação e follow-up.

### Fluxo Administrativo
1. Admin acessa painel Django para visualizar e gerenciar leads.
2. Exportação de dados para CRM externo.

## User Interface Design

### Sistema de Design Completo para Landing Page
- **Paleta de Cores**:
  - Primária: Azul Gelo (#00BFFF) - Energia e frescor.
  - Secundária: Cinza Metálico (#A9A9A9) - Profissionalismo.
  - Acentos: Verde Energético (#32CD32) para CTAs.
  - Neutros: Branco (#FFFFFF), Preto Suave (#333333).

- **Tipografia**:
  - Cabeçalhos: Montserrat Bold (Google Fonts) - Moderno e impactante.
  - Corpo: Open Sans Regular - Legível e clean.
  - Tamanhos: H1 48px, H2 32px, Body 16px.

- **Espaçamento e Grid**:
  - Grid de 12 colunas com gutters de 24px.
  - Margens verticais entre seções: 80px para separação clara.

- **Sistema de Componentes**:
  - **Botões**: Classes Tailwind como `bg-blue-500 hover:bg-blue-600 text-white py-3 px-6 rounded-lg`.
  - **Cards**: Para serviços, com sombra suave e hover effects.
  - **Formulários**: Campos com validação inline, usando Django Forms + Tailwind.
  - **Navegação**: Menu fixo com âncoras para seções.

- **Visão Geral do Design da Página**:
  - Layout vertical de scroll único com seções full-width.
  - Hero com imagem de fundo e overlay.
  - Seções alternando fundos claros/escuros para contraste.

- **Responsividade**:
  - Mobile-first: Stack seções verticalmente abaixo de 768px.
  - Breakpoints: sm (640px), md (768px), lg (1024px).

- **Otimização de Performance**:
  - Lazy loading para imagens em seções inferiores.
  - Animações suaves com Tailwind transitions.

## Technical Specifications

### Stack Técnico
- **Backend**: Django 5.x, Python 3.12+.
- **Banco de Dados**: PostgreSQL para leads (SQLite para dev).
- **Frontend**: TailwindCSS integrado via Django templates.
- **Outras Dependências**: Django Forms para validação, python-dotenv para env vars.

### Estrutura de Pastas
project_root/
  manage.py
  /core           → Configurações (settings, urls)
  /apps           
    /landing      → Models, views, templates para a landing page
  /templates      → base.html, landing.html com seções
  /static         → CSS compilado do Tailwind, JS mínimo
  requirements.txt

### Integração de API
- Endpoints Django para processamento de formulários.
- Integração com e-mail service (ex.: SendGrid) para notificações.

## Performance and SEO

### Requisitos de Performance
- Tempo de carregamento < 3s em conexões 3G.
- Otimização: Compressão de assets, minificação CSS/JS via Django pipeline.

### Requisitos de SEO
- Meta tags dinâmicas no template Django.
- Sitemap.xml gerado via Django sitemap framework.
- Structured data (JSON-LD) para serviços e contato.

## Conversion and Lead Generation

### Estratégia de Funil
- Topo: Seção Home atrai com benefícios.
- Meio: Seções Serviços e Sobre constroem confiança.
- Fundo: Seção Contato converte com formulário simples.

### Automação
- Integração com e-mail para follow-ups automáticos.

## Analytics and Success Metrics

### KPIs
- Taxa de conversão > 5%.
- Tempo na página > 2min.

### Integrações
- Google Analytics 4 para tracking de scrolls e envios de formulário.

## Acceptance Criteria and Testing

### Critérios de Aceitação
- Landing page carrega todas as seções corretamente.
- Formulário envia leads para admin.

### Testes
- Unitários: Django tests para views e forms.
- E2E: Selenium para fluxo de scroll e submissão.