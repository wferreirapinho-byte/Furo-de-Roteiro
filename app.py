import json
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Lista de filmes por categoria
filmes_por_categoria = {
    'Ação': ['Vingadores: Ultimato', 'Mad Max: Estrada da Fúria', 'John Wick'],
    'Comédia': ['Corra Que A Policia Vem Ai', 'Se Beber, Não Case', 'Superbad - É Hoje'],
    'Drama': ['A Vida É Bela', 'O Resgate Do Soldado Ryan', 'A Lista de Schindler'],
    'Terror': ['Invocação do Mal', 'O Exorcista', 'Sobrenatural'],
    'Aventura': ['Indiana Jones', 'Jurassic Park', 'Piratas do Caribe'],
    'Ficção Científica': ['Interestelar', 'Efeito Borboleta', 'A Chegada']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    filme_sugerido = None
    if request.method == 'POST':
        categoria = request.form['categoria']
        if categoria in filmes_por_categoria:
            filme_sugerido = random.choice(filmes_por_categoria[categoria])
    return render_template('index.html', filme=filme_sugerido)

# Função handler para rodar no Netlify
def handler(event, context):
    # Aqui, você pode retornar as mesmas respostas que o Flask faria
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Funcionando no Netlify!'})
    }
