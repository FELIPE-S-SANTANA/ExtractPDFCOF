import tabula
import pandas as pd

VALIDATOR = 'CONTATOR'

HEAD_COFINS = ['Modelo', 'Série', 'Número_Nota', 'Emissão','Descrição',
               'Cod_Mercadoria', 'CFOP', 'UF', 'Unidade', 'Quantidade', 'Valor', 'Diferença', 'COFINS']
NEW_HEAD_COFINS = ['Modelo', 'Série', 'Número_Nota', 'Emissão','NCM', 'Descrição',
               'Cod_Mercadoria', 'CFOP', 'UF', 'Unidade', 'Quantidade', 'Valor', 'Diferença', 'COFINS']
def format_df(row):
    if row['Descrição'].count(VALIDATOR)==1:
        index = int(row['index'])+1
        x = df.loc[df['index'] == index, 'Descrição'].values[0]
        df['NCM'] = row['Descrição'][:9]
        row['Descrição'] = row['Descrição'][8:]+x

        return row
    else:
        return 'remove'

df_result = pd.DataFrame()
PATH = "C:\\Users\\felipe.santana\\desktop\\Jobs\\Thulio\\felipe\\Laudo\\COFINS\\2010 COFINS - 10283723413201666_05673_07166_DOCUMENTOSDIVERSOS-OUTROS.PDF"
file = tabula.read_pdf(PATH, output_format='dataframe', encoding='ANSI', java_options=None, pages='all').fillna('')
for i in file:
    df = i
    df.columns = HEAD_COFINS
    df = df.drop(index=[0,1])
    df['Descrição'] = df['Descrição'].astype(str)

    df = df.reset_index()

    df = df.apply(lambda row: format_df(row), axis=1)
    df = df[~df.Descrição.str.contains("remove") == True]
    df = df[NEW_HEAD_COFINS]
    df_result = pd.concat(df_result,df)


write = pandas.ExcelWriter('C:\\Users\\felipe.santana\\desktop\\Jobs\\Thulio\\felipe\\NEW\\NEW\\2010 COFINS - 10283723413201666_05673_07166_DOCUMENTOSDIVERSOS-OUTROS.xlsx')
df.to_excel(write,'Teste', index=False)
write.save()
