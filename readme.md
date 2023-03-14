A quick and dirty script for downloading paid addons from the blendermarket.
Great if you can't be bothered manually downloading each new release.

== USAGE ==
1. Open blendermarket.com in a web browser
2. Sign in to blendermarket
3. Open networks tab, find request for blendermarket.com and paste key/value from `set-cookie` request header into a new `cookies.txt` file. You just need the `_cgc_markets_session` cookie for auth. Make sure cookies.txt is formatted like: `_cgc_markets_session=dGhlc2VhcmVub3RteWNvb2tpZXM`
4. Run script `python main.py C:/blender/addons`

Note, this script will create folders based on addon name. If you want to remap where an addon will be downloaded, just add an alias to the `name_mappings.py` file