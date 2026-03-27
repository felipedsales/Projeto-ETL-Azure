# 🚀 Projeto ETL de Ponta a Ponta: Kaggle ➡️ Azure SQL ➡️ Databricks

Este projeto demonstra a construção de um pipeline de Engenharia de Dados completo (Extração, Transformação e Carga), utilizando dados reais de atividades físicas e frequência em academias. O fluxo integra processamento local com Pandas e processamento distribuído em nuvem com Apache Spark via Databricks, tendo o Azure SQL Database como repositório central.

Este repositório é uma aplicação prática de arquitetura de dados em nuvem, governança e segurança (gerenciamento de credenciais e firewalls), refletindo cenários reais de ambientes corporativos e fundamentos de dados da Microsoft (DP-900/AZ-900).

## 🛠️ Arquitetura e Tech Stack

* **Linguagem & Ambiente:** Python 3, desenvolvido nativamente em Linux Mint via PyCharm.
* **Extração (E):** API oficial do Kaggle.
* **Transformação (T):** Pandas (limpeza de dados, padronização e criação de logs de ingestão).
* **Carga (L):** SQLAlchemy e `pyodbc` (ODBC Driver 18 for SQL Server).
* **Armazenamento em Nuvem:** Microsoft Azure SQL Database.
* **Análise Avançada:** Databricks (PySpark, conexão JDBC).
* **Segurança:** Gerenciamento de credenciais com `python-dotenv` e controle de regras de Firewall na Azure (IP whitelisting).

## 📊 O Dataset
O conjunto de dados utilizado foi o [Daily Gym Attendance and Workout Activity](https://www.kaggle.com/datasets/jayjoshi37/daily-gym-attendance-and-workout-activity-data), que contém informações detalhadas sobre rotinas de treinos, hipertrofia, frequência e volume de carga.

## ⚙️ Estrutura do Projeto

```text
projeto_etl_azure/
├── data/                   # Diretório temporário para os arquivos extraídos (ignorado no git)
├── .env                    # Variáveis de ambiente e credenciais (ignorado no git)
├── .gitignore              # Arquivos e pastas a serem ignorados pelo controle de versão
├── db_connect.py           # Módulo de conexão segura com o Azure SQL
├── kaggle_extract.py       # Módulo de comunicação com a API do Kaggle
├── main.py                 # Orquestrador do pipeline (Pandas + ETL)
└── README.md               # Documentação do projeto