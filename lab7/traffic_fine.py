def parse_ticket_id(ticket_id):
    """Parses a ticket ID string formatted as PREFIX-YEAR-SERIAL.
    Hardened against invalid format, non-string, and malformed inputs.
    """
    if not isinstance(ticket_id, str):
        return None
    parts = ticket_id.strip().split('-')
    if len(parts) != 3:
        return None
    prefix, year_str, serial_str = parts
    if not prefix or not year_str.isdigit() or not serial_str.isdigit():
        return None
    try:
        year = int(year_str)
        serial = int(serial_str)
        return prefix.upper(), year, serial
    except ValueError:
        return None


def total_fines(amounts_csv):
    """Calculates the sum of fine amounts given as a comma-separated string,
    capped at 10000.
    Hardened against empty strings, non-numeric values, and invalid formats.
    """
    if not isinstance(amounts_csv, str):
        return 0
    cleaned = amounts_csv.strip()
    if not cleaned:
        return 0
    amounts = []
    for a in cleaned.split(','):
        item = a.strip()
        if not item:
            continue
        try:
            val = int(item)
            if val < 0:
                continue
            amounts.append(val)
        except ValueError:
            continue
    total = sum(amounts)
    if total > 10000:
        total = 10000
    return total


def speed_excess(reading):
    """Calculates the percentage of speed over the limit from a 'speed/limit' string.
    Hardened against invalid formats, zero division, and non-numeric inputs.
    """
    if not isinstance(reading, str):
        return 0
    parts = reading.strip().split('/')
    if len(parts) != 2:
        return 0
    speed_str, limit_str = parts[0].strip(), parts[1].strip()
    try:
        speed = int(speed_str)
        limit = int(limit_str)
    except ValueError:
        return 0
    if limit <= 0:
        return 0
    return (speed - limit) * 100 // limit


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
