from talon.voice import Context, Key, Str

ctx = Context('words')
def shrink_word(m):
    word = str(m.dgndictation[0]._words[0]).lower()
    if not word in shrink_map:
        raise Exception('%s not in shrink map' % word)
    Str(shrink_map[word])(None)

keymap = {
    'shrink <dgndictation>': shrink_word,
}

shrink_map = {
    'administrator': 'admin',
    'alternate': 'alt',
    'apartment': 'apt',
    'applications': 'apps',
    'arguments': 'args',
    'attributes': 'attrs',
    'button': 'btn',
    'command': 'cmd',
    'compute': 'cmp',
    'context': 'ctx',
    'concatenate': 'concat',
    'configure': 'config',
    'control': 'ctrl',
    'format': 'fmt',
    'image': 'img',
    'jason': 'json',
    'message': 'msg',
    'package': 'pkg',
    'parameter': 'param',
    'source': 'src',
    'standard': 'std',
    'temporary': 'tmp',
    'text': 'txt',
    'user': 'usr',
    'user id': 'uid',
    'utilities': 'utils',
    'user': 'usr',
    'error': 'err',
    'boolean': 'bool',
    'return': 'ret',
    'package': 'pkg',
    'python': 'py',
    'random': 'rand',
    'frequency': 'freq',
    'operations': 'ops',
    'initialize': 'init',
    'iterator': 'iter',
    'vector': 'vec',
    'convolution': 'conv',
    'deconvolution': 'deconv',
    'derivative': 'deriv',
    'distribution': 'dist',
    'contribute': 'contrib',
    'delete': 'del',
    'different': 'diff',
    'square root': 'sqrt',
    'sequence': 'seq',
    'predict': 'pred',
    'ending': 'end',
    'yaml': 'yml',
    'condition': 'cond',
    'validation': 'val',
    'optimization': 'opt',
    'generator': 'gen',
    'memory': 'mem',
    'environments': 'envs',
    'environment': 'env',
    'application': 'app',
}

# TODO: allow using shrink within dictation
ctx.keymap(keymap)
