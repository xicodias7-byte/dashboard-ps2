def read_ps2_file(path):
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    header = lines[0]
    details = lines[1:-1]
    footer = lines[-1]

    return header, details, footer


def parse_amount(detail_line):
    raw = detail_line[30:43]
    return int(raw) / 100


def validate_ps2(header, details, footer):
    if header[0:3] != "PS2":
        return False

    if footer[0:3] != "PS2":
        return False

    for d in details:
        if d[0:3] != "PS2":
            return False

    expected_total = int(footer[29:42]) / 100
    expected_count = int(footer[15:29])

    real_total = sum(parse_amount(d) for d in details)
    real_count = len(details)

    return expected_total == real_total and expected_count == real_count


def load_all_files(folder="data"):
    import os

    files = [f"{folder}/{f}" for f in os.listdir(folder) if f.endswith(".ps2")]

    dataset = []

    for file in files:
        header, details, footer = read_ps2_file(file)
        if validate_ps2(header, details, footer):
            for d in details:
                amount = parse_amount(d)
                client = d[17:28]
                dataset.append({
                    "file": file,
                    "client": client,
                    "amount": amount
                })

    return dataset
