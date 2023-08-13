# import tabula
# import pandas as pd
# import numpy as np

# list_table = tabula.read_pdf('converter.pdf', pages='all', lattice=True)
# print(len(list_table))

# for table in list_table:
#     print (table)

import tabula
import pandas as pd


nameItem = str(input('digite o nome do arquivo a converter: '))

# Ler as tabelas do PDF
# list_table = tabula.read_pdf('converter.pdf', pages='all', lattice=True)
list_table = tabula.read_pdf(f'{nameItem}.pdf', pages='all')

# Criar um objeto ExcelWriter
excel_writer = pd.ExcelWriter(f'{nameItem}.xlsx', engine='xlsxwriter')

# Loop através das tabelas
for idx, table in enumerate(list_table):
    # Converter a tabela para um DataFrame do pandas
    df = pd.DataFrame(table)

    # Salvar a tabela em uma planilha do Excel
    sheet_name = f'Tabela_{idx + 1}'
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

# Fechar o ExcelWriter para salvar o arquivo Excel
excel_writer.close()

print("Tabelas salvas em " f'{nameItem}'".xlsx")