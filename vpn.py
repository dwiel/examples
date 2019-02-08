import os
import time
from talon.voice import Context, Key, press

ctx = Context("")


def connect_to_vpn(m):
    os.system("automator ~/start_vpn.workflow")


def disconnect_from_vpn(m):
    os.system("automator ~/start_vpn.workflow")
    stop_proxy(None)


def stop_proxy(m):
    os.system("osascript -e 'quit app \"Proxifier\"'")


def start_proxy(m):
    os.system('open -a "Proxifier"')
    time.sleep(0.2)
    press("cmd-tab")


keymap = {
    "connect to vpn": connect_to_vpn,
    "disconnect from vpn": disconnect_from_vpn,
    "stop proxy": stop_proxy,
    "start proxy": start_proxy,
}

ctx.keymap(keymap)
