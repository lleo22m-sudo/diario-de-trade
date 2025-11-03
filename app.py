import sqlite3
import os
from flask import Flask, render_template

app = Flask(__name__)

# O Render precisa que o banco de dados seja salvo em um local persistente
# Usaremos 'trades.db' no diretório raiz do projeto
DATABASE = 'trades.db'

def init_db():
    # Esta função garante que o arquivo trades.db e a tabela 'trades' existam.
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY,
            ativo TEXT NOT NULL,
            entrada_preco REAL,
            saida_preco REAL,
            pips_ganhos REAL,
            drawdown_max REAL,
            potencial_pos REAL,
            data_registro TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Chamada para inicializar o DB quando o Flask inicia
with app.app_context():
    init_db()

# --- 1. Rota Principal (Frontend) ---
@app.route('/')
def index():
    # Esta rota renderiza o HTML que será o nosso formulário/dashboard
    return render_template('index.html')


# --- 2. Rota de Health Check (Recomendado para Render) ---
# Serve para o Render checar se o serviço está no ar
@app.route('/health')
def health_check():
    return "OK", 200


# --- 3. Execução Local ---
if __name__ == '__main__':
    # Se você for rodar no seu computador (para testes), use o comando: python app.py
    # O Render ignora esta parte e usa o Gunicorn
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 5000))