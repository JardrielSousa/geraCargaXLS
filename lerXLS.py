import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão com o PostgreSQL
db_user = "postgres"
db_password = "postgres"
db_host = "localhost"  # ou IP do servidor
db_port = "5432"  # Porta padrão do PostgreSQL
db_name = "postgres"

# Criar a engine do SQLAlchemy
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Criar um DataFrame de exemplo
#data = {"id": [1, 2, 3], "nome": ["Alice", "Bob", "Charlie"]}
data = {"id": [3], "nome": ["usuario"],"idade" : 30}
df = pd.DataFrame(data)

# Inserir os dados no PostgreSQL (substitua 'sua_tabela' pelo nome correto)
df.to_sql("usuario", engine, if_exists="append", index=False)

print("Dados inseridos com sucesso!")
