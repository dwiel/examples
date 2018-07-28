from talon.voice import Context, Key, Str
from user import std
import string

ctx = Context('talon_editor')

def key(m):
    words = [str(word).lower() for word in m._words]
    modifiers = []
    if 'command' in words:
        modifiers.append('cmd')
    if 'shift' in words:
        modifiers.append('shift')
    if 'control' in words or 'alt' in words:
        modifiers.append('alt')

    key = None
    for word in words:
        if word in alnum:
            key = alnum[word]
        if word in string.ascii_lowercase:
            key = word

    if key is None:
        print('no key', words)
        return

    Str("Key('{}')".format('-'.join(modifiers + [key])))(None)


alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = dict(list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)])
letters = '({})'.format(' | '.join(alpha_alt + list(string.ascii_uppercase)))

ctx.keymap({
    'key (command | shift | control | alt)* ' + letters: key,
    'keymap <dgndictation>': ("'", std.text, "': ,", Key('left')),
    'map string <dgndictation>': ("'", std.text, "': ,", "'", std.text, "'"),
})
