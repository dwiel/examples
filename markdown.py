from os import system
from talon.voice import Context, Key

ctx = Context('markdown')

keymap = {
    'markdown check': '- [ ] ',
}

ctx.keymap(keymap)
