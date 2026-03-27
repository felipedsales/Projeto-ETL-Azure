import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def get_db_engine():
    """Cria e devolve a engine de conexão com o Azure SQL de forma segura."""

    # URL.create gerencia espaços, caracteres especiais e a formatação do driver automaticamente
    connection_url = URL.create(
        "mssql+pyodbc",
        username=os.getenv('AZURE_USER'),
        password=os.getenv('AZURE_PASSWORD'),
        host=os.getenv('AZURE_SERVER'),
        database=os.getenv('AZURE_DATABASE'),
        query={
            "driver": "ODBC Driver 18 for SQL Server",
            "TrustServerCertificate": "yes"
        }
    )

    return create_engine(connection_url)


def load_to_azure(df: pd.DataFrame, table_name: str):
    """Carrega o DataFrame para o Azure SQL Database."""
    print(f"Conectando ao Azure SQL e iniciando a carga na tabela: {table_name}...")

    engine = get_db_engine()

    try:
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print("Carga finalizada com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")


def testar_ligacao():
    """Testa se a conexão ao Azure SQL Database está funcionando."""
    print("Iniciando o teste de conexão ao Azure...")
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            resultado = conn.execute(text("SELECT @@VERSION"))
            versao = resultado.fetchone()
            print("\n✅ Conexão bem-sucedida!")
            print(f"Versão do Servidor Azure:\n{versao[0]}")
    except Exception as e:
        print(f"\n❌ Erro ao conectar ao Azure SQL:\n{e}")


if __name__ == "__main__":
    testar_ligacao()