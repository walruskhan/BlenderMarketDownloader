import argparse
from argparse import ArgumentParser
import blendermarket
import os
import pathlib
import re
import requests
import subprocess
import cookies
from uuid import uuid4
import name_mappings

parser = argparse.ArgumentParser(
    prog = "BlenderMarket Downloader",
    description = "Downloads purchased addons")
parser.add_argument('destination', help="Destination folder to download to")
parser.add_argument('-whatif', help='Dont download', action='store_true')

def main():
    args = parser.parse_args()
    print(args.destination)
    print(args.whatif)

    # blendermarket.listOrders()
    # purchases = blendermarket.getPurchasesFromOrder('https://blendermarket.com/pickup/b92lhp')
    # print(list(xs))

    purchases = blendermarket.getPurchases()
    # print(list(purchases))

    if os.path.exists('logs.txt'):
        os.remove('logs.txt')
    with open('logs.txt', 'a') as fh_log:
        for x in purchases:
            addon_name = x[0]
            store_page = x[1]
            assets = x[2]

            folder_name = name_mappings.rename(addon_name)
            fh_log.write(f"'{addon_name}' -> '{folder_name}'\n")
            path = os.path.join(args.destination, folder_name)
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)

            with open(os.path.join(path, 'blendermarket.url'), 'w') as fd:
                fd.write("[{" + str(uuid4()) + "}]\n")
                fd.write(f"Prop3 = 19, 2\n")
                fd.write(f"[InternetShortcut]]\n")
                fd.write(f"IDList =\n")
                fd.write(f"URL = {store_page}")

            for asset in assets:
                asset_name = re.sub(r'\s+', '-', asset[0])
                url = asset[1]

                asset_path = os.path.join(path, asset_name)
                if (os.path.exists(asset_path)):
                    print(f"skipping '{asset_name}' because it already exists in {asset_path}")
                    continue

                # [{000214A0 - 0000 - 0000 - C000 - 000000000046}]
                # Prop3 = 19, 2
                # [InternetShortcut]
                # IDList =
                # URL = http: // www.google.com /

                if not args.whatif:
                    print(f"downloading '{asset_name}' to {asset_path}")
                    r = requests.get(url, cookies=cookies.cookies)


                    r = requests.get(r.url)
                    with open(asset_path, 'wb') as fd:
                        for chunk in r.iter_content(chunk_size=128):
                            fd.write(chunk)
                else:
                    print(f"[whatif] download '{asset_name}' to {asset_path}")






if __name__ == '__main__':
    main()
