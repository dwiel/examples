from talon.voice import Context, Key, press
from talon import ctrl

initialize = [Key('cmd-l'), Key('tab'), Key('escape')]
vi_mode = [Key('i')]

def heading(count):
    def function(m):
        press('cmd-left')
        [press('=') for _ in range(count)]
        press('space')
        press('cmd-right')
        press('space')
        [press('=') for _ in range(count)]
        [press('left') for _ in range(count + 1)]
    return function

ctx = Context('colony_wiki', func=lambda app, win:
              'The Colony Wiki' in win.title)
ctx.keymap({
    # custom helpers
    'heading one': heading(1),
    'heading two': heading(2),
    'heading three': heading(3),
    'heading for': heading(4),

    'insert list': [Key('cmd-left'), '  * '],

    # general mode
    'save page': Key('ctrl-alt-s'),
    'go to root': Key('ctrl-alt-x'),
    'go to home': Key('ctrl-alt-h'),
    'edit page': Key('ctrl-alt-e'),
    'show page': Key('ctrl-alt-v'),
    'focus search': Key('ctrl-alt-f'),
    'show revisions': Key('ctrl-alt-o'),
    '[show] recent changes': Key('ctrl-alt-r'),
    # edit mode
    'preview page': Key('ctrl-alt-p'),
    'insert link': Key('ctrl-alt-l'),
})
