from talon.voice import Context, Key

ctx = Context('media')

ctx.keymap({
    'media play': Key('cmd-shift-1'),
    'media pause': Key('cmd-shift-7'),
    'media next': Key('cmd-shift-2'),
    'media previous': Key('cmd-shift-9'),
    'media like': Key('cmd-shift-8'),
})
