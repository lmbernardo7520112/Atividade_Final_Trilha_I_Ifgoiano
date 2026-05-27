import nbformat
import pytest
import os

def test_notebook_visual_contract():
    notebook_path = "notebooks/Trabalho_Trilha_I_AcolheMente_PB.ipynb"
    assert os.path.exists(notebook_path), "Notebook not found"
    
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        
    code_cells = [c.source for c in nb.cells if c.cell_type == 'code']
    markdown_cells = [c.source for c in nb.cells if c.cell_type == 'markdown']
    all_cells = code_cells + markdown_cells
    full_text = " ".join(all_cells)
    
    # 1. existe célula contendo referência ao logo institucional
    assert any("logo" in c.lower() and ("goiano" in c.lower() or "urutai" in c.lower()) for c in code_cells), \
        "Missing logo download comment"
    
    # 2. existe célula contendo `logo_urutai.png`
    assert any("logo_urutai.png" in c for c in code_cells), "Missing logo download URL/code"
    
    # 3. existe referência ao IF Goiano
    assert "IF Goiano" in full_text, "Missing 'IF Goiano'"
    
    # 4. existe seção de apresentação do aluno
    assert any("Apresentação do Aluno" in c for c in markdown_cells), \
        "Missing 'Apresentação do Aluno' section"
    
    # 5. existe referência textual a Profile/Lattes ou síntese equivalente
    assert "Leonardo Maximino Bernardo" in full_text, "Missing student name"
    
    # 6. existe seção de variáveis proposicionais
    assert "Variáveis Proposicionais" in full_text, "Missing 'Variáveis Proposicionais' section"
    
    # 7. existem E, B, V, S, C, I, A no notebook
    for var in ["E", "B", "V", "S", "C", "I", "A"]:
        assert var in full_text, f"Missing variable {var}"
        
    # 8. existem R1–R6
    for i in range(1, 7):
        assert f"R{i}" in full_text, f"Missing rule R{i}"
        
    # 9. existe CNF
    assert "CNF" in full_text, "Missing CNF reference"
    
    # 10. existe seção de não diagnóstico
    assert "NÃO diagnostica" in full_text or "não diagnostica" in full_text.lower(), \
        "Missing non-diagnostic claim"
    
    # 11. existe seção de governança LGPD/ECA/PSE
    assert "LGPD" in full_text and "ECA" in full_text and "PSE" in full_text, \
        "Missing Governance LGPD/ECA/PSE"
    
    # 12. não existem caminhos absolutos
    assert "file:///home" not in full_text, "Found absolute path"
    
    # 13. não existe `.gemini`
    assert ".gemini" not in full_text, "Found .gemini"
    
    # 14. o notebook possui pelo menos uma imagem ou HTML de capa institucional
    assert "<img" in full_text or "<div" in full_text or "includegraphics" in full_text or "titlepage" in full_text, "Missing cover image"
