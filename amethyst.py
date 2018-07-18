from talon.voice import Key, Context

ctx = Context('amethyst')


# def text_to_number(m, numwords={}):
#     tmp = [str(s).lower() for s in m.dgndictation[0]._words]
#     words = [parse_word(word) for word in tmp]
#
#     # Special case to set volume to max
#     if "hundred" in words:
#         return 100
#
#     if not numwords:
#         units = [
#             "zero", "one", "two", "three", "four", "five", "six",
#             "seven", "eight", "nine", "ten", "eleven", "twelve",
#             "thirteen", "fourteen", "fifteen", "sixteen",
#             "seventeen", "eighteen", "nineteen"
#         ]
#
#         tens = [
#             "", "", "twenty", "thirty", "forty", "fifty",
#             "sixty", "seventy", "eighty", "ninety"
#         ]
#
#         for idx, word in enumerate(units):
#             numwords[word] = (1, idx)
#         for idx, word in enumerate(tens):
#             numwords[word] = (1, idx * 10)
#
#     result = 0
#     for word in words:
#         if word not in numwords:
#             return -1
#
#         scale, increment = numwords[word]
#         result = result * scale + increment
#
#     return result
#
#
# def parse_word(word):
#     word = word.lstrip('\\').split('\\', 1)[0]
#     return word
#
#
# def desk(m):
#     number = text_to_number(m)
#     Key('ctrl-{}'.format(number))(None)


keymap = {
    # 'desk <dgndictation>': desk,

    'window next screen': Key('ctrl-alt-shift-l'),
    'window previous screen': Key('ctrl-alt-shift-h'),
    'window next': Key('alt-shift-j'),
    'window previous': Key('alt-shift-k'),
    'window move desk': Key('ctrl-alt-shift-h'),

    'window full': Key('alt-shift-d'),
    'window tall': Key('alt-shift-a'),
    'window middle': Key('alt-shift-`'),
    'window move main': Key('alt-shift-enter'),
    'window grow': Key('alt-shift-l'),
    'window shrink': Key('alt-shift-h'),
}

single_digits = '123456789'
keymap.update({'desk %s' % digit: Key('ctrl-%s' % digit) for digit in single_digits})
keymap.update({'window move desk %s' % digit: Key('ctrl-alt-shift-%s' % digit) for digit in single_digits})

screen_mapping = {
    '1': 'w',
    '2': 'e',
    '3': 'r',
    '4': 't',
}
keymap.update({'window screen %s' % digit: Key('ctrl-alt-shift-%s' % digit) for digit in '1234'})

ctx.keymap(keymap)
