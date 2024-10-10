#RM 99094 LUCAS VINICIUS DE ALMEIDA BRIGIDA
#RM 551410 JOÃO VICTOR 

import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport

# Carregar o dataset Titanic diretamente com seaborn
df = sns.load_dataset('titanic')

# Gerar o relatório de perfil dos dados
profile = ProfileReport(df, title="Relatório de Profiling", explorative=True)

# Salvar o relatório em formato HTML
output_html_path = "relatorio_profiling.html"
profile.to_file(output_html_path)

print(f"Relatório gerado com sucesso: {output_html_path}")