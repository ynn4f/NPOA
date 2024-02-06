import json
import requests
import threading
import concurrent.futures
import argparse

def callAPI(command, params):
    URLprefix = 'https://stat.ripe.net/data/'
    URLsuffix = '/data.json'

    r = requests.get(url = URLprefix + command + URLsuffix, params = params, timeout = 15.0)

    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        return None

outputLock = threading.Lock()

def grabPrefixes(ASN, output_file):
    global outputLock

    print('Grabbing prefixes for ASN', ASN)
    ASNdetails = callAPI('ris-prefixes', {'resource': ASN, 'list_prefixes': True})
    if ASNdetails != None:
        with open(output_file, 'w') as f:
            for prefix in ASNdetails['data']['prefixes']['v4']['originating']:
                print(ASN, ": ", prefix)
                outputLock.acquire()
                f.write("%s\n" % prefix)
                outputLock.release()

def main():
    parser = argparse.ArgumentParser(description='Fetch CIDRs for an AS number.')
    parser.add_argument('-n', '--asn', type=str, required=True, help='AS number to fetch CIDRs for (e.g., AS****)')
    args = parser.parse_args()

    output_file = f"{args.asn}.txt"

    ASNlist = callAPI('as-overview', {'resource': args.asn})

    if ASNlist != None:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(lambda asn: grabPrefixes(asn, output_file), [args.asn])

if __name__ == "__main__":
    main()
