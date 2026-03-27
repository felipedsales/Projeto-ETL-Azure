import os
import pandas as pd

# Importando as funções dos arquivos que já criamos
from kaggle_extract import extract_from_kaggle
from db_connect import load_to_azure


def transform_data(csv_path: str) -> pd.DataFrame:
    """Aplica regras de limpeza e transformação usando Pandas."""
    print(f"Iniciando a transformação. Lendo o arquivo: {csv_path}...")

    # Lê o CSV
    df = pd.read_csv(csv_path)

    # --- Regras de Transformação (T) ---

    # 1. Padronização técnica: colunas em minúsculo e sem espaços (facilita o SQL)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # 2. Qualidade de dados: remover linhas completamente vazias
    df = df.dropna(how='all')

    # 3. Governança: adicionar uma coluna de controle com a data da ingestão
    df['data_ingestao_etl'] = pd.Timestamp.now()

    print(f"Transformação concluída! Total de registros prontos para o banco: {len(df)}")
    return df


def run_pipeline():
    """Orquestra as etapas de Extração, Transformação e Carga."""

    # --- Parâmetros do Projeto ---
    DATASET_REF = 'jayjoshi37/daily-gym-attendance-and-workout-activity-data'
    PASTA_DESTINO = './data'
    TABELA_DESTINO = 'tb_gym_activity'

    # IMPORTANTE: Você precisa verificar o nome exato do CSV que foi baixado na pasta 'data'
    NOME_ARQUIVO_CSV = f'{PASTA_DESTINO}/daily_gym_attendance_workout_data.csv'

    print("\n" + "=" * 40)
    print("🚀 INICIANDO PIPELINE ETL DE PONTA A PONTA")
    print("=" * 40 + "\n")

    # 1. Extração (Kaggle -> Local)
    extract_from_kaggle(DATASET_REF, PASTA_DESTINO)

    # 2. Transformação (Local -> Pandas DataFrame)
    # Aqui o código vai falhar se o NOME_ARQUIVO_CSV estiver incorreto
    df_transformado = transform_data(NOME_ARQUIVO_CSV)

    # 3. Carga (Pandas DataFrame -> Azure SQL)
    load_to_azure(df_transformado, TABELA_DESTINO)

    print("\n" + "=" * 40)
    print("✅ PIPELINE FINALIZADO COM SUCESSO!")
    print("=" * 40)


if __name__ == "__main__":
    run_pipeline()