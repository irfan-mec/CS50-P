import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: The number of Bitcoins must be a number.")
        sys.exit(1)

    try:

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        price_usd = data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error: Failed to retrieve Bitcoin price. {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Unexpected response format from API.")
        sys.exit(1)


    total_cost = num_bitcoins * price_usd


    print(f"Cost of {num_bitcoins:.4f} Bitcoins in USD: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()