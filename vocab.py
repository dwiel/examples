from talon.engine import engine
add_words = [
    # r'dockerfile',
    # r'docker file\dockerfile',
    # r'jace on\json',
    # r'mobile shell\mosh',
    # r'virtual env\virtualenv',
    # r'typed_word\spoken word'
    # r''
]
remove_words = [
    # r'(\left-parenthesis\left paren',
    # r'(\left-parenthesis\left parenthesis',
    # r')\right-parenthesis\right paren',
    # r')\right-parenthesis\right parenthesis',
    # r'[\left-square-bracket\left bracket',
    # r']\right-square-bracket\right bracket',
]
def on_ready(j):
    if add_words:
        engine.cmd('w.add', words=add_words)
    if remove_words:
        engine.cmd('w.remove', words=remove_words)

engine.register('ready', on_ready)

"""
    # miscellaneous
    'chuck': 'shock'
    'aldo': 'algo'
    'GPUs': 'gpus'
    'docker file': 'dockerfile'
    'deck': 'deque'
    'compose a bull': 'composable'
    'jace on': 'json'

    # linux
    'H top': 'htop'
    'IO top': 'iotop'
    'T mucks': 'tmux'
    'mobile shell': 'mosh'
    'dot shell': '.sh'

    # python
    'virtual env': 'virtualenv'
    'V env': 'venv'
    'pie V env': 'pyvenv'
    'dot pie': '.py'
    'pie dot test': 'py.test'
    'pie test': 'pytest'
    'python three': 'python3'
    'X fail': 'xfail'
    'in it': 'init'
    'L if': 'elif'
    'K wargs': 'kwargs'
    'is instance': 'isinstance'
    'numb pie': 'numpy'
    'matt plot lib': 'matplotlib'
    'see pickle': 'cPickle'
    'pie plot': 'pyplot'
    'hyper opt': 'hyperopt'
    'D type': 'dtype'

    # names
    'the wheel': 'dwiel'
    'Z the wheel': 'zdwiel'
    'shayna': 'shaina'
    'R june': 'arjun'
    'hareenee': 'harini'
    'it I': 'itai'

    # ngraph
    'N graph': 'ngraph'
    'make access': 'make axis'
    'angie': 'NG'

    # deep learning
    'see far': 'cifar'
    'theeano': 'theano'
    'tensor flow': 'tensorflow'
    'tensor board': 'tensorboard'
    'py torch': 'pytorch'
    'open AI': 'openai'
    'RMS prop': 'rmsprop'
    'soft max': 'softmax'
    'tan H': 'tanh'
    'bit coin': 'bitcoin'
    'readit': 'reddit'
    'farm bought': 'farmbot'
    'nvidia SMI': 'nvidia-smi'
    'log its': 'logits'
    'a fine': 'affine'
    'D convolution': 'deconvolution'
    'math some': 'sum'
    'mini grid': 'minigrid'

    # sgi
    'D space': 'dspace'
    'P pham': 'PFAM'
    'P phams': 'PFAMs'

"""
