import argparse
from argparse import ArgumentParser
import blendermarket
import os
import pathlib
import re
import requests
import subprocess
import cookies

parser = argparse.ArgumentParser(
    prog = "BlenderMarket Downloader",
    description = "Downloads purchased addons")
parser.add_argument('destination', help="Destination folder to download to")

def main():
    args = parser.parse_args()
    print(args.destination)

    # blendermarket.listOrders()
    # purchases = blendermarket.getPurchasesFromOrder('https://blendermarket.com/pickup/b92lhp')
    # print(list(xs))

    purchases = blendermarket.getPurchases()
    # print(list(purchases))

    for x in purchases:
        addon_name = x[0]
        assets = x[1]


        folder_name = re.sub(r'[|.,+!@&*:;=&^%$#]+', '', addon_name)
        folder_name = re.sub(r'[\s\-]+', '-', folder_name)
        path = os.path.join(args.destination, folder_name)
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        for asset in assets:
            asset_name = re.sub(r'\s+', '-', asset[0])
            url = asset[1]

            asset_path = os.path.join(path, asset_name)
            if (os.path.exists(asset_path)):
                print(f"skipping '{asset_name}' because it already exists in {asset_path}")
                continue

            print(f"downloading '{asset_name}' to {asset_path}")
            r = requests.get(url, cookies=cookies.cookies)
            r = requests.get(r.url)
            with open(asset_path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)






if __name__ == '__main__':
    main()
