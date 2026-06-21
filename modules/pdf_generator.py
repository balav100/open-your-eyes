from fpdf import FPDF


def save_braille_as_pdf(braille_text, output_path):

    pdf = FPDF()

    pdf.add_page()

    # Add Unicode Font
    pdf.add_font(
        "DejaVu",
        "",
        "assets/DejaVuSans.ttf",
        uni=True
    )

    pdf.set_font(
        "DejaVu",
        size=14
    )

    lines = braille_text.split("\n")

    for line in lines:

        pdf.multi_cell(
            0,
            10,
            line
        )

    pdf.output(output_path)

    return output_path