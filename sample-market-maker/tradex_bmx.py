from market_maker.market_maker import ExchangeInterface
from market_maker.ws.ws_thread import BitMEXWebsocket
from market_maker.bitmex import BitMEX
import settings
import keyboard

def handler(msg):
    print(msg)


if __name__ == "__main__":
    bmx = BitMEX(settings.BASE_URL, settings.SYMBOL, settings.API_KEY, settings.API_SECRET)
    keyboard.add_hotkey('p', lambda: bmx.place_order(1, 7250))

    # topics = ["chat"]
    # ws = BitMEXWebsocket(topics, handler)
    # ws.connect("wss://testnet.bitmex.com/realtime", "XBTUSD", False)
    keyboard.wait()