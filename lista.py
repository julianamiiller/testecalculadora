from fpdf import FPDF

# Conteúdo da lista
titulo = "Lista 6 – Funções do 2º Grau (Nova Versão)"
instrucoes = "Resolva os exercícios a seguir com atenção, mostrando todos os cálculos e justificativas necessárias."

questoes = [
    "1) Determine os pontos de intersecção da parábola da função f(x) = x² – 6x + 8 com o eixo das abscissas.",
    "2) Resolva a equação 3x² + 2x – 1 = 0.",
    "3) Qual das funções a seguir representa o gráfico abaixo? (Esboce o gráfico de cada alternativa)\nA) f(x) = x² – 2x – 3\nB) f(x) = x² + 2x + 3\nC) f(x) = 2x² – 4x + 1\nD) f(x) = 3x² + x – 6",
    "4) O custo de fabricação de um item é dado por C(x) = x² – 10x + 25. Qual é a quantidade de itens a ser produzida para que o custo seja nulo?",
    "5) Assinale a alternativa que corresponde ao gráfico da função f(x) = –x² + 4x – 3.",
    "6) Sobre a função 2x² – 3x – 2, assinale a alternativa correta:\nA) As raízes não são reais.\nB) O gráfico é uma parábola com concavidade para cima.\nC) A soma das raízes é –3.\nD) A função é constante.",
    "7) A altura de um foguete após o lançamento é dada por h(t) = –5t² + 20t. Determine:\na) O instante em que o foguete atinge o solo.\nb) A altura máxima alcançada.",
    "8) Determine o valor de k para que a função f(x) = x² + 2x + k não tenha raízes reais.",
    "9) Para quais valores de m a função f(x) = (m + 1)x² – 3x + 4 possui raízes reais?",
    "10) O gráfico da função y = x² – 4x + m toca o eixo x em apenas um ponto. Qual o valor de m?",
    "11) Um corpo é lançado verticalmente e sua altura é dada por y = –16x² + 64x. Calcule o tempo no ar e a altura máxima.",
    "12) A temperatura de um paciente variou com o tempo conforme uma função quadrática. A 0h estava com 37°C, a 1h com 38,5°C, e a 2h com 39°C. Encontre a função T(t).",
    "13) O lucro de uma empresa é dado por L(x) = –2x² + 24x – 40. Determine o número de unidades que maximiza o lucro e qual é esse lucro.",
    "14) Sobre a função f(x) = –x² + 8x – 12, marque as afirmativas verdadeiras:\nA) O vértice é (4, 4).\nB) A função é sempre negativa.\nC) O conjunto imagem é {y ∈ R | y ≤ 4}.\nD) A função cresce até x = 4 e depois decresce.",
    "15) Uma empresa vende x centenas de produtos. A receita é dada por R(x) = 10x² – 30x + 200, e o custo por C(x) = 6x² – 18x + 100. Para qual x o lucro é máximo?"
]

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, titulo, ln=True, align='C')

pdf.ln(5)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, instrucoes)

pdf.ln(5)
for questao in questoes:
    pdf.multi_cell(0, 10, questao)
    pdf.ln(2)

# Salvando o PDF
nome_arquivo = "Lista_6_Funcoes_2Grau_Nova.pdf"
pdf.output(nome_arquivo)

print(f"PDF gerado com sucesso: {nome_arquivo}")
