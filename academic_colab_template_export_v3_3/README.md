# academic_colab_template_export_v3_3

Variante demonstrativa do notebook AcolheMente v3.3 com exportação para PDF via `nbconvert + article + xelatex`, seguindo a mesma pipeline do template `Resposta_Trabalho_Trilha_I.ipynb`.

## Propósito

Demonstrar que o notebook AcolheMente é funcional e exportável no Colab, seguindo o padrão pedagógico do template da Trilha I.

**Este PDF NÃO substitui o PDF formal abnTeX2 v3.3** (`main_acolhemente_abntex2.pdf`, 72 páginas).

## Estrutura

```
academic_colab_template_export_v3_3/
├── notebooks/   → Notebook demonstrativo com pipeline de exportação
├── outputs/     → PDF article, .tex intermediário, log
├── scripts/     → Script local de build
├── audits/      → Engenharia reversa, quality gate, resumo, fala oral
└── README.md
```

## Como usar

### No Google Colab
1. Abra o notebook em `notebooks/`
2. Execute todas as células
3. O PDF será gerado automaticamente na última célula

### Localmente
```bash
python3 scripts/build_article_pdf_from_notebook.py
```

## Relação com o PDF formal

| Artefato | Classe | Páginas | Função |
|----------|--------|---------|--------|
| PDF article (este) | `article` | ~16 | Demonstração de exportabilidade do notebook |
| PDF abnTeX2 (v3.3) | `abntex2` | 72 | Documento formal de submissão |
