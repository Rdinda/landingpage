SHELL := pwsh

# Ajuste PYTHON se necessário. Por padrão usa o Python do venv local.
PYTHON ?= python
MANAGE := $(PYTHON) manage.py

##
## Comandos de DESENVOLVIMENTO (Windows)
## Execute estes dois alvos em terminais separados.
##
.PHONY: dev-run dev-tailwind dev-start
dev-run:
	$(MANAGE) runserver 0.0.0.0:8000

dev-tailwind:
	$(MANAGE) tailwind start

# Alias para conveniência; executa o mesmo que dev-tailwind
dev-start: dev-tailwind
	@echo "Tailwind watcher iniciado. Em outro terminal, execute 'make dev-run' para subir o Django."

## 
## Tailwind CLI Standalone (instalação e build)
## 
.PHONY: tailwind-install tailwind-build
tailwind-install:
	$(MANAGE) tailwind install

tailwind-build:
	$(MANAGE) tailwind build

## 
## Coleta de estáticos para PRODUÇÃO
## Requer STATIC_ROOT configurado (já definido em setup/settings.py)
## 
.PHONY: collectstatic prod-build
collectstatic:
	$(MANAGE) collectstatic --noinput

prod-build:
	$(MANAGE) tailwind build
	$(MANAGE) collectstatic --noinput

## 
## Utilitários
## 
.PHONY: clean-static version help
clean-static:
	@echo "Removendo pasta STATIC_ROOT (staticfiles)..."
	if (Test-Path staticfiles) { Remove-Item -Recurse -Force staticfiles }

version:
	$(PYTHON) -c "import importlib.metadata as m; print('django-tailwind', m.version('django-tailwind'))"

help:
	@echo "Targets disponíveis:"
	@echo "  dev-run          -> inicia o servidor Django (http://localhost:8000)"
	@echo "  dev-tailwind     -> inicia o watcher do Tailwind (standalone)"
	@echo "  dev-start        -> alias de dev-tailwind"
	@echo "  tailwind-install -> baixa/instala a CLI standalone do Tailwind v4"
	@echo "  tailwind-build   -> gera CSS otimizado (produção)"
	@echo "  collectstatic    -> coleta arquivos estáticos em STATIC_ROOT"
	@echo "  prod-build       -> build do Tailwind + collectstatic (pipeline de produção)"
	@echo "  clean-static     -> remove a pasta STATIC_ROOT (staticfiles)"
	@echo "  version          -> mostra versão do django-tailwind"
	@echo "  help             -> mostra esta ajuda"