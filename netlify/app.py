import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bem-vindo ao Flask no Netlify!"

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Funcionando!'})
    }

if __name__ == '__main__':
    app.run(debug=True)
