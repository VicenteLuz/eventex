* Eventex
Sistema de eventos encomendado pela Morena

** Como desenvolver?

1. Clone o repositorio,
2. Crie um virtualenv com phyton 3.5
3. Ative o Virtualenv.
4. Instale as dependencias
5. Configure a instancia com .env
6. Execute os testes

'''Console
git clone git@github.com.br:VicenteLuz/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
'''

** Como fazer o deploy
1. Crie uma instancia no heroku.
2. Envie as configuraçoes para heroku.
3. Defina uma secret key segura.
4. Defina DEBUG=False.
5. Configure um servico de E-mail.
6. Envie o codigo para heroku.

'''Console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o Email
git push heroku --force
'''