# AS CIDR Fetcher

AS CIDR Fetcher is a Python script that retrieves CIDRs (Classless Inter-Domain Routing) associated with a specified Autonomous System (AS) number using RIPEstat's API. It allows you to quickly fetch and save CIDRs to a text file for further analysis or use.

## Usage

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

```sh
python script.py -n AS****
```

Replace `AS****` with the desired Autonomous System (AS) number.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Options

- `-n, --asn`: Specifies the AS number for which CIDRs need to be fetched.

## Example

```sh
python script.py -n AS12345
```

This will fetch CIDRs associated with the AS number `AS12345` and save them to a text file named `AS12345.txt`.

## License

This project is not licensed, and you are free to use, modify, and distribute it as you wish.

## Acknowledgements

- This script utilizes the RIPEstat API for retrieving AS CIDRs.
