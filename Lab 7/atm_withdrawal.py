
def notes_needed(amount):
    if not isinstance(amount, str):
        return 0

    amount = amount.replace(",", "").strip()

    if not amount.isascii() or not amount.isdigit():
        return 0

    return int(amount) // 100


def mask_card(card_number):
    if not isinstance(card_number, str):
        return "Invalid Card"

    groups = card_number.split()

    if len(groups) != 4:
        return "Invalid Card"

    if not all(
        len(group) == 4 and group.isascii() and group.isdigit()
        for group in groups
    ):
        return "Invalid Card"

    return "XXXX XXXX XXXX " + groups[3]


def average_withdrawal(amounts_csv):
    if not isinstance(amounts_csv, str):
        return 0

    parts = amounts_csv.split(",")

    if not all(
        part.strip().isascii() and part.strip().isdigit()
        for part in parts
    ):
        return 0

    amounts = [int(part.strip()) for part in parts]

    return sum(amounts) // len(amounts)
