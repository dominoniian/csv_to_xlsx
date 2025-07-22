import csv
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import argparse

def converter_csv_para_xlsx(arquivo_csv, arquivo_xlsx=None, encoding='iso-8859-1'):
    """Converte CSV delimitado por ; para XLSX com formatação"""
    if not arquivo_xlsx:
        arquivo_xlsx = arquivo_csv.replace('.csv', '.xlsx')
    
    pasta = Workbook()
    planilha = pasta.active
    
    try:
        with open(arquivo_csv, 'r', encoding=encoding) as arquivo:
            leitor = csv.reader(arquivo, delimiter=';', quotechar='"')
            
            # Cabeçalhos em negrito
            cabecalhos = next(leitor)
            planilha.append(cabecalhos)
            
            for celula in planilha[1]:
                celula.font = Font(bold=True)
                celula.alignment = Alignment(wrap_text=True)
            
            # Processa linhas de dados
            for linha in leitor:
                planilha.append(linha)
        
        # Ajusta largura das colunas
        for coluna in planilha.columns:
            tamanho_max = 0
            for celula in coluna:
                try:
                    tamanho = len(str(celula.value))
                    if tamanho > tamanho_max:
                        tamanho_max = tamanho
                except:
                    pass
            planilha.column_dimensions[coluna[0].column_letter].width = min(tamanho_max + 2, 30)
        
        pasta.save(arquivo_xlsx)
        print(f"✅ Conversão concluída: '{arquivo_csv}' → '{arquivo_xlsx}'")
    
    except Exception as erro:
        print(f"❌ Erro: {str(erro)}")
        print("Dicas:")
        print("- Verifique o encoding do arquivo (tente -e utf-8)")
        print("- Confira se o CSV usa delimitador ; corretamente")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conversor CSV para Excel para dados brasileiros")
    parser.add_argument("arquivo_csv", help="Caminho do arquivo CSV de entrada")
    parser.add_argument("-o", "--output", help="Caminho do arquivo XLSX de saída (opcional)")
    parser.add_argument("-e", "--encoding", help="Encoding do arquivo (padrão: iso-8859-1)", default="iso-8859-1")
    
    args = parser.parse_args()
    converter_csv_para_xlsx(args.arquivo_csv, args.output, args.encoding)