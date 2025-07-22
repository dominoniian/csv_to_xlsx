# Conversor CSV para Excel (XLSX)

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![OpenPyXL](https://img.shields.io/badge/dependency-openpyxl-green)

Um conversor simples e eficiente para transformar arquivos CSV em planilhas Excel (XLSX), otimizado para dados brasileiros.

---

## 📋 Pré-requisitos

- Python 3.6 ou superior  
- Biblioteca `openpyxl`

Instale a dependência com:

```bash
pip install openpyxl
```

---

## 🚀 Como Usar

### ✅ Conversão Básica

```bash
python csv_xlsx.py arquivo.csv
```

Isso criará um arquivo `arquivo.xlsx` no mesmo diretório.

---

### ⚙️ Opções Avançadas

| Opção | Descrição                                 | Exemplo                                               |
|-------|-------------------------------------------|-------------------------------------------------------|
| `-o`  | Nome personalizado para o arquivo de saída| `python csv_xlsx.py dados.csv -o resultado.xlsx`      |
| `-e`  | Especificar encoding (padrão: iso-8859-1) | `python csv_xlsx.py dados.csv -e utf-8`               |

---

## ✨ Funcionalidades

✔ Conversão rápida de arquivos `.csv` para `.xlsx`  
✔ Suporte completo a caracteres PT-BR (acentos, ç)  
✔ Formatação automática:
- Cabeçalhos em **negrito**
- Ajuste inteligente da **largura das colunas**

✔ Preserva números com **vírgula decimal**  
✔ Compatível com arquivos delimitados por `;`

---

## 🛠 Solução de Problemas

| Problema Comum         | Solução                                                      |
|------------------------|--------------------------------------------------------------|
| Erro de encoding       | Tente usar `-e utf-8` ou `-e latin1`                          |
| Arquivo não encontrado | Verifique o caminho e permissões do arquivo                  |
| Delimitador incorreto  | Confirme se o CSV utiliza `;` como separador                |
| Erro em linha específica| Verifique dados inconsistentes na linha mencionada          |

---
