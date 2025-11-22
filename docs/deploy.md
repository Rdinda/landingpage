Guia de execução e deploy (Django + Tailwind v4 standalone)

Ambientes
- Desenvolvimento (Windows):
  - Em um terminal: `make dev-run` (inicia Django em http://localhost:8000/)
  - Em outro terminal: `make dev-tailwind` (inicia o watcher do Tailwind) — você também pode usar o alias `make dev-start`.
  - Observação: no Windows, use `tailwind start` (o `tailwind dev` não é suportado pelo django-tailwind).

- Build rápido (validação local):
  - `make tailwind-build` (gera o CSS otimizado em theme/static/css/dist/styles.css)

- Produção:
  1) Certifique-se de que `STATIC_ROOT` está configurado (já definido em `setup/settings.py` como `staticfiles`).
  2) Execute `make prod-build` para:
     - Gerar o CSS do Tailwind: `python manage.py tailwind build`
     - Coletar estáticos para `STATIC_ROOT`: `python manage.py collectstatic --noinput`
  3) Sirva os arquivos estáticos de `STATIC_ROOT`:
     - Opção simples: Whitenoise (adicionar middleware e configurar para produção)
     - Opção recomendada para escala: Servir via servidor web (Nginx/Apache) ou CDN/S3 (definindo `STATIC_URL` para o endpoint da CDN e publicando o conteúdo de `staticfiles`).

Notas importantes
- O app Tailwind configurado é `theme` (`TAILWIND_APP_NAME = 'theme'`). O CSS gerado fica em `theme/static/css/dist/styles.css` e é incluído automaticamente nos templates via `{% tailwind_css %}`.
- O arquivo `theme/static_src/src/styles.css` contém o `@source` apontando para os templates, JS e arquivos Python, garantindo que as classes sejam varridas para geração do CSS.
- Em CI/CD, padronize: `make prod-build` antes do passo de deploy. Assim, o pacote resultante já tem os estáticos otimizados.
- Caso precise de plugins Tailwind avançados no futuro, avalie se a CLI standalone atende à necessidade; se não, considere fluxo via npm. Enquanto isso, mantenha o pipeline simples e sem dependências de Node.