import pdfplumber
import pandas as pd
import zipfile

def main():

    pdf_endereco = r"C:\Users\Win 10 Pro\Desktop\Nova pasta (2)\teste-intuitive-care-2\anexo1.pdf"


    todas_tabelas = []
    with pdfplumber.open(pdf_endereco) as pdf:
        for pagina in pdf.pages:
            tabelas_pagina = pagina.extract_tables()
            for tabela_individual in tabelas_pagina:
                    todas_tabelas.extend(tabela_individual)

                    tabelas_pagina = pagina.extract_tables()




    if todas_tabelas:

        df = pd.DataFrame(todas_tabelas[1:], columns=todas_tabelas[0])

        df.replace({"OD": "Outros Procedimentos", "AMB": "Ambulatorial"}, inplace=True)


        csv_filename = 'anexo1.csv'
        df.to_csv(csv_filename, index=False, encoding='utf-8')


        zip_filename = "Teste_anderson.zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_filename)
        print(f"Arquivo CSV compactado em {zip_filename} com sucesso!")
    else:
        print("Nenhuma tabela foi encontrada no PDF.")


if __name__ == "__main__":
    main()
