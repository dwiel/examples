container template = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
{vocabulary}
  </array>
</dict>
</plist>
"""

vocabulary_template = """<dict>
  <key>Version</key>
  <string>3.0/1</string>
  <key>Words</key>
  <array>
  <dict>
  <key>EngineFlags</key>
  <integer>17</integer>
  <key>Flags</key>
  <string></string>
  <key>Sense</key>
  <string></string>
  <key>Source</key>
  <string>User</string>
  <key>Spoken</key>
  <string>{spoken}</string>
  <key>Written</key>
  <string>{written}</string>
</dict>"""

vocabulary = [
'PWD',

'IO',
'smartnav',
'pip',
'pip install',
'brew install',
'ncloud',
'ipython',
'iter',
'pull request',
'SGI',
'DQN',
'LSTM',
'RNN',
'KNN',
'GRU',
'GPU',
'SGD',
'word2vec',
'op graph',
'initializer',
'keras',
'tensorflow',
'matmul',
'frontends',
'refactor',
'contrib',
'expand dims',
'gan',
'NG',
'NP',
'minibatch',
'SSH',
'rebase'
'affine',
'affine layer',
'affine embedding',
'linear layer',
'argmax',
'encode',
'onehot',
'multihot',
'embeddings',
'embedder',
'embedders',
'cart pole',
'end to end',
'unordered axes',
'voicecode',
'convolution',
'convolutional',
'conv',
'conv net',
'yinyin',
'channel yinyin',
'fiaz',
'mergeable',
'docker',
'IU',
'folsom',
'folsom lab',
'IPFS',
'hyper parameter',
'hyper parameters',

'epsilon',
'start epsilon',
'end epsilon',
'model end',
'decay',
'embedder',
'ethereum',

'yield',
'python3'

'bit flip',
'gym bit flip',
]
vocabularyAlternate:
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
