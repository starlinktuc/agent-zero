import requests
import re

def validate_cuit(cuit):
    # CUIT format: 11 digits with a specific structure
    # First 2 digits: 20, 23, 24, 27, 30, 33, or 34
    # Next 8 digits: Any digits
    # Last digit: Check digit
    pattern = re.compile(r'^(20|23|24|27|30|33|34)\d{8}\d$')
    if pattern.match(cuit):
        return True
    return False

def get_contribuyente(cuit):
    if not validate_cuit(cuit):
        return "CUIT number with No Valid Format."

    url = f"https://www.tangofactura.com/Rest/GetContribuyenteWithImpuestosAndvencimientos?cuit={cuit}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
cuit_number = "20317656506"
result = get_contribuyente(cuit_number)
print(result)