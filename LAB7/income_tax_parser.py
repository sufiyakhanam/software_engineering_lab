
def clean_pan(pan):
    """
    Removes spaces from a PAN, upper-cases it and validates its format.
    Returns None for invalid input.
    """
    if not isinstance(pan, str):
        return None

    pan = pan.strip().replace(' ', '').upper()

    if len(pan) != 10:
        return None

    if not (pan[:5].isalpha() and pan[:5].isascii()
            and pan[5:9].isdigit() and pan[5:9].isascii()
            and pan[9].isalpha() and pan[9].isascii()):
        return None

    return pan

def parse_amount(text):
    """
    Converts an amount such as 'Rs 12,50,000' into an int.
    Returns None for invalid input.
    """
    if not isinstance(text, str):
        return None

    text = text.replace('Rs', '').replace(',', '').strip()

    if not text or len(text) > 18 or not text.isascii() or not text.isdecimal():
        return None

    return int(text)


def parse_tax_slab(line):
    """
    Parses 'LOW-HIGH:RATE' into a (low, high, rate) tuple.
    Returns None for invalid input.
    """
    if not isinstance(line, str):
        return None

    try:
        limits, rate = line.split(':')
        low, high = limits.split('-')

        low = int(low.strip())
        high = int(high.strip())
        rate = int(rate.strip())

        if low < 0 or high < 0 or rate < 0 or rate > 100 or low > high:
            return None

        return low, high, rate

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running clean_pan ====")
    value = input("Enter a PAN (e.g. abcde 1234f): ")
    print("Cleaned PAN:", clean_pan(value))

    print("\n==== Running parse_amount ====")
    value = input("Enter an amount (e.g. Rs 12,50,000): ")
    print("Amount in rupees:", parse_amount(value))

    print("\n==== Running parse_tax_slab ====")
    value = input("Enter a tax slab as LOW-HIGH:RATE (e.g. 250000-500000:5): ")
    print("Tax slab (low, high, rate):", parse_tax_slab(value))


if __name__ == "__main__":
    main()
