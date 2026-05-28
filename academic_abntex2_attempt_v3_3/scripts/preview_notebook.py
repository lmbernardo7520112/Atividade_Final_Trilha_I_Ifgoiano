import json
import sys

nb_path = "academic_abntex2_attempt_v2/notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print("# Estrutura do Notebook: Trabalho_Trilha_I_AcolheMente_PB.ipynb\n")
print(f"**Total de células:** {len(nb['cells'])}\n")

for i, cell in enumerate(nb['cells']):
    ctype = cell['cell_type']
    print(f"## Célula {i+1} [{ctype.upper()}]")
    source = "".join(cell['source'])
    
    if ctype == "markdown":
        lines = source.split("\n")
        if len(lines) > 12:
            print("\n".join(lines[:12]))
            print("\n*... [texto truncado para exibição] ...*\n")
        else:
            print(source + "\n")
    else:
        print("```python")
        lines = source.split("\n")
        if len(lines) > 15:
            print("\n".join(lines[:15]))
            print("# ... [código truncado para exibição] ...")
        else:
            print(source)
        print("```\n")
    print("---\n")
