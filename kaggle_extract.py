import os
from kaggle.api.kaggle_api_extended import KaggleApi


def extract_from_kaggle(dataset_ref: str, download_path: str = './data'):
    """
    Conecta na API do Kaggle, baixa e descompacta o dataset especificado.
    dataset_ref: formato 'usuario/nome-do-dataset'
    """
    print(f"Iniciando a extração do dataset: {dataset_ref}...")

    try:
        # A API lê automaticamente o ~/.kaggle/kaggle.json do Linux Mint
        api = KaggleApi()
        api.authenticate()

        # Cria a pasta de destino (ex: ./data) se ela não existir
        os.makedirs(download_path, exist_ok=True)

        # Faz o download e já descompacta o .zip
        api.dataset_download_files(dataset_ref, path=download_path, unzip=True)

        print(f"✅ Extração concluída com sucesso! Arquivos salvos na pasta '{download_path}'")

    except Exception as e:
        print(f"❌ Erro ao extrair dados do Kaggle:\n{e}")


# Bloco para testar o download isoladamente
if __name__ == "__main__":
    # Variável de teste - vamos substituir pelo seu dataset real
    DATASET_EXEMPLO = 'jayjoshi37/daily-gym-attendance-and-workout-activity-data'

    print("Testando módulo de extração...")
    extract_from_kaggle(DATASET_EXEMPLO)