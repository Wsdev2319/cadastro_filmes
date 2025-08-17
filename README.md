<h1 align="center">🎬 Cadastro de Filmes</h1>

<p align="center">
  Sistema simples em Python para cadastrar, atualizar, listar e excluir filmes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite&logoColor=orange" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

---

<h2>💡 Descrição</h2>
<p>
Este projeto é um sistema para gerenciar filmes usando <strong>Python</strong> e <strong>SQLite</strong>. 
O objetivo é praticar manipulação de dados, formulários e integração com banco de dados.
</p>



<h2>✨ Funcionalidades</h2>
<ul>
  <li>Cadastrar novos filmes</li>
  <li>Atualizar informações de filmes existentes</li>
  <li>Listar todos os filmes cadastrados</li>
  <li>Excluir filmes do banco de dados</li>
  <li>Armazenamento local em arquivo <code>SQLite</code> (<code>titulo.db</code>)</li>
</ul>

---

<h2>🛠 Tecnologias utilizadas</h2>
<ul>
  <li>Python 3.x</li>
  <li>SQLite (via módulo <code>sqlite3</code>)</li>
  <li>Estrutura modular (cada funcionalidade em um arquivo separado)</li>
</ul>

---

<h2>📂 Estrutura do projeto</h2>

<pre>
Cadastro_filmes/
│
├─ .venv/                  # Ambiente virtual (não versionado)
├─ Dados_str.py            # Manipulação de dados de filmes
├─ atualiza.py             # Atualizar filmes
├─ dados.py                # Funções de acesso aos dados
├─ db.py                   # Configuração do banco de dados
├─ excluir.py              # Excluir filmes
├─ form.py                 # Interface / formulários
├─ leitura.py              # Listar filmes
├─ tabela.py               # Estrutura ou tabela de filmes
├─ requirements.txt        # Dependências
└─ titulo.db               # Banco de dados SQLite
</pre>

---

<h2>⚡ Como usar</h2>

<pre>
git clone https://github.com/Wsdev2319/cadastro_filmes.git
cd Cadastro_filmes

# Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar scripts
python Dados_str.py
python atualiza.py
python leitura.py
</pre>

---

<h2>ℹ️ Observações</h2>
<ul>
  <li>A pasta <code>.venv</code> está ignorada pelo Git</li>
  <li>O banco <code>titulo.db</code> é criado automaticamente</li>
  <li>Projeto ideal para aprendizado de Python e SQLite</li>
</ul>

---

<h2>👤 Autor</h2>
<p><strong>Wsdev2319</strong></p>

<p align="center">
  <a href="https://github.com/Wsdev2319"><img src="https://img.shields.io/badge/GitHub-Wsdev2319-181717?logo=github&logoColor=white" alt="GitHub"></a>
</p>

├─ requirements.txt # Dependências do projeto
└─ titulo.db # Banco de dados SQLite


