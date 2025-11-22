## Perguntas de Esclarecimento

1. Preferência de compilação Sass: Node (Dart Sass) ou Python (`django-sass-processor`)? com python
2. Quais páginas/templates são prioridade para manter paridade visual imediata (home, landing, forms)? landing
3. Há diretrizes de branding existentes (paleta, tipografia, espaçamentos) que devemos seguir? sim. as que ja estao definidas no projeto.
4. Componentes essenciais: quais precisam existir no v1 (botões, navbar, cards, formulários, tabelas, modais)? navbar, cards, botoes, forms.
5. Requisitos de acessibilidade (WCAG nível alvo) e suporte cross-browser esperados? wcag nível a, suporte chrome, firefox, safari, edge.
6. Podemos manter `django_browser_reload` em dev e desativar Node completamente após migração? sim.

## Visão Geral

* Objetivo: substituir Tailwind por um design system próprio em Sass, mantendo paridade visual e simplificando manutenção.

* Princípios: tokens de design centralizados, utilitários mínimos, componentes reutilizáveis, BEM, builds diferenciados para dev/prod.

## Estratégia de Compilação Sass

* Opção A (recomendada se já aceitarmos Node): Dart Sass via script NPM para `scss → css`, sourcemaps em dev, minificação em prod.

* Opção B (menos dependências Node): `django-sass-processor` + `libsass` (manutenção do libsass é limitada). Integra-se bem ao pipeline do Django, porém pode ficar atrás do Dart Sass em features.

* Sugestão inicial: Opção A (Dart Sass), pela robustez e por já existir ambiente Node; revisitar remoção de Node após estabilização.

## Estrutura do Design System

* Diretório: `theme/static_src/scss/`

* Arquivos:

  * `_tokens.scss`: cores, espaçamentos, tipografia e z-index (portar paleta `primary` do Tailwind atual).

  * `_mixins.scss`: helpers (media queries, centralização, truncamento, foco visível).

  * `_utilities.scss`: utilitários essenciais (margens/padding discretos, `d-flex`, `justify/align`, `text-*`).

  * `_components.scss`: botões, navbar, cards, forms (estados, tamanhos, variações).

  * `_layout.scss`: grid responsivo simples (cols, gaps) e containers.

  * `main.scss`: importa os módulos acima.

* Saída: `theme/static/css/dist/main.css`.

## Fases de Migração

* Fase 1: Preparação

  * Definir pipeline Sass (A ou B), scripts de build/watch, sourcemaps em dev, minificação em prod.

  * Configurar inclusão do CSS novo nos templates base; manter Tailwind ativo temporariamente para migração incremental.

* Fase 2: Tokens e Fundamentos

  * Portar paleta `primary` do Tailwind (`theme/static_src/src/styles.css`) para `_tokens.scss`.

  * Definir tipografia base, escala de espaçamentos, bordas, sombras.

* Fase 3: Utilitários Essenciais

  * Implementar utilitários de layout e espaçamento equivalentes aos mais usados do Tailwind (mapeamento 1:1 quando possível).

  * Documentar convenções de nomes e limites de escala (evitar explosão de classes).

* Fase 4: Componentes

  * Botões (variações `primary`, `secondary`, `outline`), inputs/labels/feedback, navbar, cards.

  * Estados de foco/acessibilidade e responsividade.

* Fase 5: Remapeamento de Templates

  * Substituir classes Tailwind por utilitários/componentes Sass nos templates prioritários (`theme/templates/base.html`, `landing/templates/landing/base.html`).

  * Validar visual parity página a página.

* Fase 6: Limpeza

  * Remover `{% tailwind_css %}`, dependências `tailwind`/`@tailwindcss/cli`, e refs no `settings.py`.

  * Garantir `collectstatic` funcional para `main.css` e auditoria de tamanho.

## Compatibilidade Django

* Dev: manter `django_browser_reload` ativo; watcher Sass pelo NPM ou pela integração escolhida.

* Prod: build minificado, `STATIC_ROOT`/`collectstatic` e cache-control adequados (via `whitenoise` ou servidor HTTP).

## Critérios de Aceite

* Paridade visual ≥ 95% nas páginas prioritárias.

* Lighthouse performance/acessibilidade em linha ou superior ao estado atual.

* CSS final ≤ 200KB gzip (ajustável conforme escopo).

* Sem regressões de responsividade em breakpoints principais.

## Riscos & Mitigações

* Explosão de utilitários: limitar escala e incentivar componentes.

* Divergência visual: checklist de tokens e revisão de UI por página.

* Dependência de Node: optar pela estratégia B se preferirmos reduzir dependências.

## Próximos Passos

* Responder às perguntas de esclarecimento.

* Escolher a estratégia de compilação Sass (A ou B).

* Após sua aprovação, inicio a Fase 1 e reporto conclusão/ próximos passos por fase.

