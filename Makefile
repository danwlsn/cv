include .env

pdf-build: pdf/cv-latest.pdf
	@echo "Build complete."

pdf/cv-latest.pdf: cv.yaml
	./pdf/scripts/build.sh

.PHONY: open-latest
open-latest: pdf/cv-latest.pdf
	open pdf/cv-latest.pdf

api-build: api/app.tar.gz
	@echo "API BUILD COMPLETE"

api/app.tar.gz: api/api/*.py api/requirements.txt
	mkdir -p build
	cp api/requirements.txt build
	cp api/gunicorn_conf.py build
	cp cv.yaml build
	cp -r api/api build
	tar -czf api/app.tar.gz build
	rm -rf build api/requirements.txt

api/requirements.txt: api/pyproject.toml
	poetry -C api export -o api/requirements.txt

.PHONY: api-serve
api-serve:
	poetry -C api run fastapi dev api/api/main.py

.PHONY: api-deploy
api-deploy: api/app.tar.gz
	poetry -C api run fab --prompt-for-sudo-password -r api -H $(DEPLOY_USER)@$(DEPLOY_ADDR) deploy-api

