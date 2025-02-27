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

# ler excel
df = pd.read_excel("usuario.xlsx", sheet_name="Planilha1", skiprows=1)  # Ajuste o nome da aba se necessário

# Inserir os dados no PostgreSQL (substitua 'sua_tabela' pelo nome correto)
df.to_sql("usuario", engine, if_exists="append", index=False)

print("Dados inseridos com sucesso!")
