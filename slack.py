from talon.voice import Context, Key

ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    'channel': Key('cmd-k'),
    'channel up': Key('alt-up'),
    'channel down': Key('alt-down'),
    '(highlight command | insert command)': ['``', Key('left')],
    '(highlight code | insert code)': ['``````', Key('left left left')],

    'baxley': Key('cmd-['),
    'fourthly': Key('cmd-]'),
    'goneck': Key('shift-alt-down'),
    'gopreev': Key('shift-alt-up'),

    'toggle sidebar': Key('cmd-.'),
}

ctx.keymap(keymap)
