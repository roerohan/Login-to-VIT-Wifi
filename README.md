# VIT Wifi Login

Run this python script to login to VIT wifi automatically when connected.

- `vit_wifi_login.py` - uses requests (no browser)
- `selenium_vit_wifi_login.py` - uses selenium (with browser)

Change the .get("//link") and element names to reuse the script to login to other places.

To run, you need:
1. Python3
2. pip3

To get selenium:
```
pip install selenium
```

Get chromedriver here:
http://chromedriver.chromium.org/
Add this chromedriver to path.

To run the file, open a terminal in this directory: "path/to/directory/Login-to-Wifi" and run python login_to_wifi.py
