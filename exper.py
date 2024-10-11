""" import re

def convert_to_latex(expr):
    # Aggiungere spazi attorno agli operatori per facilità di parsing
    expr = re.sub(r'([*^/])', r' \1 ', expr)

    # Gestione delle potenze: sostituire `a^b` con `a^{b}`
    expr = re.sub(r'(\d+)\s*\^\s*(\d+)', r'\1^{\2}', expr)

    # Sostituire divisione generale con \frac{numerator}{denominator}
    expr = re.sub(r'^{(.+)}\s*/\s*(.+)$', r'\\frac{\1}{\2}', expr)

    # Sostituire divisioni specifiche con \frac{a}{b} all'interno dell'espressione
    expr = re.sub(r'(\[[^\]]+\]|\([^()]+\)|\d+)\s*/\s*(\[[^\]]+\]|\([^()]+\)|\d+)', r'\\frac{\1}{\2}', expr)

    # Sostituire moltiplicazione con \times
    expr = expr.replace('*', '\\times')

    # Aggiungere parentesi graffe attorno a somme complesse
    expr = re.sub(r'(\([^()]+\))', r'{\1}', expr)

    # Sostituire parentesi quadre e tonde con quelle in stile LaTeX
    expr = expr.replace('[', '\\left[').replace(']', '\\right]')
    expr = expr.replace('(', '\\left(').replace(')', '\\right)')

    return expr

# Esempio di utilizzo:
espressione = "{[(9/2 + 2)] * 4^3}/2^2"
latex = convert_to_latex(espressione)
print(latex)
"""


""" def convert_to_latex(expr):
    # Aggiungere spazi attorno agli operatori per facilità di parsing
    expr = re.sub(r'([*^/])', r' \1 ', expr)

    # Gestione delle potenze: sostituire `a^b` con `a^{b}`
    expr = re.sub(r'(\d+)\s*\^\s*(\d+)', r'\1^{\2}', expr)

    # Sostituire divisione generale con \frac{numerator}{denominator}
    expr = re.sub(r'^{(.+)}\s*/\s*(.+)$', r'\\frac{\1}{\2}', expr)

    # Sostituire divisioni specifiche con \frac{a}{b} all'interno dell'espressione
    expr = re.sub(r'(\[[^\]]+\]|\([^()]+\)|\d+)\s*/\s*(\[[^\]]+\]|\([^()]+\)|\d+)', r'\\frac{\1}{\2}', expr)

    # Sostituire moltiplicazione con \times
    expr = expr.replace('*', '\\times')

    # Aggiungere parentesi graffe attorno a somme complesse
    expr = re.sub(r'(\([^()]+\))', r'{\1}', expr)

    # Sostituire parentesi quadre e tonde con quelle in stile LaTeX
    expr = expr.replace('[', '\\left[').replace(']', '\\right]')
    expr = expr.replace('(', '\\left(').replace(')', '\\right)')

    return expr

# Esempio di utilizzo:
espressione = "{[(9/2 + 2)] * 4^3}/2^2"
latex = convert_to_latex(espressione)
print(latex)
"""  ##okkk 
import re
import matplotlib.pyplot as plt
def pdfimg(latex_expr):
    plt.text(0.1, 0.5, f"${latex_expr}$", fontsize=18)
    plt.axis('off')
    plt.show()
def convert_to_latex(expr):
    # Aggiungere spazi attorno agli operatori per facilità di parsing
    expr = re.sub(r'([*^/+])', r' \1 ', expr)
    print(f"70  expr ",expr)

    # Gestione delle potenze: sostituire `a^b` con `a^{b}`
    expr = re.sub(r'(\d+)\s*\^\s*(\d+)', r'\1^{\2}', expr)
    print(f"74  expr ",expr)
    # Sostituire divisione generale con \frac{numerator}{denominator}
    expr = re.sub(r'^{(.+|-)}\s*/\s*(.+)$', r'\\frac{\1}{\2}', expr)
    print(f"77  expr ",expr)
    # Sostituire divisioni specifiche con \frac{a}{b} all'interno dell'espressione
    expr = re.sub(r'(\[[^\]]+\]|\([^()]+\)|\d+)\s*/\s*(\[[^\]]+\]|\([^()]+\)|\d+)', r'\\frac{\1}{\2}', expr)
    print(f"80  expr ",expr)
    # Sostituire moltiplicazione con \times
    expr = expr.replace('*', '\\times')
    print(f"83  expr ",expr)
    # Aggiungere parentesi graffe attorno a somme complesse
    expr = re.sub(r'(\([^()]+\))', r'{\1}', expr)
    print(f"86  expr ",expr)
    # Sostituire parentesi quadre e tonde con quelle in stile LaTeX
    expr = expr.replace('[', '\\left[').replace(']', '\\right]')
    print(f"89  expr ",expr)
    expr = expr.replace('(', '\\left(').replace(')', '\\right)')

    return expr

# Esempio di utilizzo:
espressione = "{[(9/2 + 2)] * 4^3}/2^2"
# espressione = " 2/3+9/7"
# espressione = "2/3-9/7"
# espressione = "  2/3-5/7*7^2  "
# espressione = "  2/5+(2/3+9/7)  "
# espressione = " [(9/2+ 4/7)-10)]*4^3 "
# espressione = "[(9/2+ 4/7)-10)]"
# espressione = " (9/2 +2)*4^3 "
latex = convert_to_latex(espressione)
print(latex)

pdfimg(latex)

# Visualizza il risultato in una finestra matplotlib


