import os
from talon.voice import Context, Key

ctx = Context('')

keymap = {
    # 'connect to vpn': os.system('automator ~/start_vpn.workflow'),
    # 'stop proxy': os.system('osascript -e \'quit app "Proxifier 2"\''),
    # 'start proxy': os.system('application:switch-to-previous')
}

ctx.keymap(keymap)


# Package.command 'connect-to-vpn',
#  spoken: 'connect to vpn'
#  description: 'connect to cisco any connect vpn'
#  enabled: true
#  action: ->
#    @exec 'automator ~/start_vpn.workflow'
#
# Package.command 'stop-proxy',
#  spoken: 'stop proxy'
#  enabled: true
#  action: ->
#    @exec 'osascript -e \'quit app "Proxifier 2"\''
#
# Package.command 'start-proxy',
#  spoken: 'start proxy'
#  enabled: true
#  action: ->
#    @exec 'open -a "Proxifier 2"'
#    @delay 200
#    @do 'application:switch-to-previous'
#
# Package.command 'disconnect-from-vpn',
#  spoken: 'disconnect from vpn'
#  description: 'disconnect from cisco any connect vpn'
#  enabled: true
#  action: ->
#    @exec 'automator ~/start_vpn.workflow'
#    @do 'user:settings:stop-proxy'
#   #  @delay 1000
#   #  @do 'connect-to-local-unison'
#
# Package.command 'connect-to-local-unison',
#    spoken: 'connect to local unison'
#    description: 'connect to local unison'
#    enabled: true
#    action: ->
#      @exec 'unison gym-arm ssh://dwiel@a//home/dwiel/src/gym-arm -repeat 1 -ignore "Path {venv}"'
