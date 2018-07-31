from talon.engine import engine
add_words = [
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
