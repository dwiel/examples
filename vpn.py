import os
from talon.voice import Context, Key

ctx = Context('')

def connect_to_vpn(m):
    os.system('automator ~/start_vpn.workflow')

def disconnect_from_vpn(m):
    os.system('automator ~/start_vpn.workflow')
    stop_proxy(None)

def stop_proxy(m):
    os.system('osascript -e \'quit app "Proxifier 2"\'')

def start_proxy(m):
    os.system('open -a "Proxifier 2"')
    time.sleep(0.2)
    press('cmd-tab')

keymap = {
    'connect to vpn': connect_to_vpn,
    'disconnect from vpn': disconnect_from_vpn,
    'stop proxy': stop_proxy,
    'start proxy': start_proxy,
}

ctx.keymap(keymap)
