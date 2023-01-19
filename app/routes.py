from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p> Ana Roberta Andrade - Designer Gráfico </p>
  </body>
</html>
    '''
@app.route('/contato')
def contato():
  return "84999819055"
@app.route('/sobre')
def sobre():
  return "sobre"

