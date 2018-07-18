ctx = Context('all')

keymap = {
    'page up': Key('pageup'),
    'page down': Keith('pagedown'),

    'ricky': Key('ctrl-e'),
    'lefty': Key('ctrl-a'),

    'shock': Key('enter'),

    'swipe': ', ',

    'posh': ["''", Key('left')],
    # TODO: test above

    
}
ctx.keymap(keymap)
