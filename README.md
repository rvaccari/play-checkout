# Bem vindo ao Play Checkout


**Stack**
- Linguagem: Python 3.9
- Frameworks: Django, Django-Ninja, Pytest
- Infra: Docker, docker-compose

**Instalação**
1. Clone o repositório
2. Execute a pré-instalação
3. Execute a instalação
4. Configure a instância com o .env
5. Execute os testes

```
git clone https://github.com/rvaccari/play-checkout.git && cd play-checkout
make pre-install
make install
make configure
make test
```

**Executando a aplicação**
```
make run
curl -X POST http://127.0.0.1:8000/checkout/api/v1/ -d '{"products": [{"id": 1, "quantity": 1}]}'
```

**Documentação**
```
make run
```
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Executando via docker-compose**
1. Clone o repositório
2. Execute o build
3. Rode o projeto
4. Pare a execução do projeto
```
git clone https://github.com/rvaccari/play-checkout.git && cd play-checkout
make docker-build
make docker-up
make docker-stop
```