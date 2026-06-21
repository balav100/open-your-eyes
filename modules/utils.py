import os



def save_output(text):

    output_path = os.path.join(
        "outputs",
        "braille_output.txt"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

    return output_path


