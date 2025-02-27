# 📌 Projeto: Análise de Dados com Docker, Python (Pandas) e PostgreSQL

## 📖 Descrição
Este projeto utiliza **Docker**, **Python (com Pandas)** e **PostgreSQL** para armazenar e analisar dados de forma eficiente. A aplicação permite a leitura de arquivos CSV, inserção de dados em um banco PostgreSQL e realização de consultas para análise de dados.

---

## 🚀 Tecnologias Utilizadas
- **Docker**: Para containerização do ambiente.
- **Python**: Linguagem principal do projeto.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados.
- **SQLAlchemy**: ORM para comunicação com o PostgreSQL.

---

## 📦 Estrutura do Projeto
```
📂 projeto
│-- 📂 data                 # Diretório para armazenar arquivos CSV
│-- 📂 db                   # Configuração do banco de dados
│   │-- init.sql            # Script SQL para criação de tabelas
│-- lerXLS.py               # Script para carregar CSV e inserir no PostgreSQL
│-- docker-compose.yml      # Configuração do ambiente Docker
│-- requirements.txt        # Dependências do projeto
│-- README.md               # Documentação do projeto
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ **Clonar o repositório**
```bash
git clone https://github.com/JardrielSousa/geraCargaXLS.git
cd geraCargaXLS
```

### 2️⃣ **Criar e iniciar os containers**
```bash
docker-compose up -d
```
Isso iniciará o **PostgreSQL** e o **Python** dentro de um ambiente Docker.

### 3️⃣ **Instalar dependências no container Python**
```bash
docker exec -it python_container pip install -r requirements.txt
```

---

## 🗄️ Banco de Dados
A base de dados é inicializada automaticamente pelo Docker. O script `init.sql` cria a seguinte tabela:
```sql
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT
);
```

### **Acessar o banco de dados PostgreSQL**
```bash
docker exec -it postgres psql -U postgres -d usuario
```

Para listar as tabelas:
```sql
\dt
```

---

## 📊 Executar o Script Python
O script **importar_dados.py** lê um arquivo CSV e insere os dados no PostgreSQL.
```bash
docker exec -it python_container python lerXLS.py
```

---

## 🛠️ Comandos Úteis
### **Parar os containers**
```bash
docker-compose down
```

### **Reiniciar o PostgreSQL**
```bash
docker restart postgres_container
```

---

## 📌 Autor
- [Jardriel Sousa](https://github.com/JardrielSousa)

Se precisar de ajuda, sinta-se à vontade para abrir uma issue! 🚀
