# Raspberry Pi Live Stocks

This is the source code which will turn your Raspberry Pi with it's display into a live exchange rates display. Your screen should be at least 500x500 in resolution.

# Initialization

-   Create a file called `APIKEYS.py` in the root folder, and then inside that file, export your API key (You can get your API key from here: https://free.currencyconverterapi.com/free-api-key). The final file should look like this: `freecurrencyconverterapi = "YOUR_API_KEY_HERE"`
-   Install `pygame` and `requests` dependencies. This command should generally work: `python -m pip install --upgrade pygame requests`
-   On Linux, you also need to run this command on your terminal: `sudo apt-get install libsdl-ttf2.0.0`
