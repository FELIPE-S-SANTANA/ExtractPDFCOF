import tabula
import pandas



VALIDATOR = 'CONTATOR'
HEAD_COFINS = ['Modelo', 'Série', 'Número', 'Dia da', 'Código', 'Descrição da Mercadoria', 'Código da Mercadoria',
               'Código', 'UF', 'Unidade', 'Quantidade', 'Valor Unitário', 'Diferença', 'COFINS']

description = ''
dif = ''
cofins = ''
flag = 0


def format_df(row):
    global description, dif, cofins
    if str(row['Descrição da Mercadoria']).count(VALIDATOR) and row['Modelo'] != '':
        return row
    elif str(row['Descrição da Mercadoria']).count(VALIDATOR) and row['Modelo'] == '':
        description = row['Descrição da Mercadoria']
        return row
    elif not str(row['Descrição da Mercadoria']).count(VALIDATOR) and row['Modelo'] != '':
        row['Descrição da Mercadoria'] = description+row['Descrição da Mercadoria']
        row['Diferença'] = dif
        row['COFINS'] = cofins
        return row
    elif row['Modelo'] == '' and row['Diferença'] != '':
        dif = row['Diferença']
        cofins = row['COFINS']
        return row
    else:
        return row


file = "C:\\Users\\felipe.santana\\desktop\\Jobs\\Thulio\\felipe\\Laudo\\COFINS\\2009 COFINS - 10283723413201666_05189_05672_DOCUMENTOSDIVERSOS-OUTROS.PDF"
print('Reading File')
df = tabula.read_pdf(file, output_format='dataframe', encoding='ANSI', java_options=None).fillna('') #pages='all'
print('Formating File')
# df = df.apply(lambda row: format_df(row), axis=1)
# df = df.loc[(df['Modelo'] != '') & (df['Modelo'] != 'Modelo')]

#
# write = pandas.ExcelWriter('C:\\Users\\felipe.santana\\desktop\\Jobs\\Thulio\\felipe\\NEW\\NEW\\10283723413201666_05189_05672_DOCUMENTOSDIVERSOS-OUTROS.xlsx')
# df.to_excel(write,'Teste', index=False)
# write.save()

