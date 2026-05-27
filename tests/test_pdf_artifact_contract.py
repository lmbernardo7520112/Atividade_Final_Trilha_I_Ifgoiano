import os
import PyPDF2

def test_pdf_artifact_contract():
    pdf_path = "reports/pdf/Trabalho_Trilha_I_AcolheMente_PB.pdf"

    # PDF existe;
    assert os.path.exists(pdf_path), "PDF file not found"

    # PDF tem tamanho mínimo razoável (ex: > 10KB)
    file_size = os.path.getsize(pdf_path)
    assert file_size > 10000, f"PDF file size too small: {file_size} bytes"

    # Verifica o número de páginas e o conteúdo
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)

        # PDF não é apenas 1–2 páginas;
        assert num_pages >= 3, f"PDF has only {num_pages} pages, expected at least 3"

        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    # PDF contém “IF Goiano”;
    assert "IF Goiano" in text or "Instituto Federal Goiano" in text, "Missing 'IF Goiano' in PDF"

    # PDF contém “AcolheMente Escolar PB”;
    assert "AcolheMente Escolar PB" in text, "Missing 'AcolheMente Escolar PB' in PDF"

    # PDF contém “Leonardo Maximino Bernardo”.
    assert "Leonardo Maximino Bernardo" in text, "Missing 'Leonardo Maximino Bernardo' in PDF"
