from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

mapping = {
    'semicolon': ';',
    r'new-line': '\n',
    r'new-paragraph': '\n\n',
}

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

# Ask for forgiveness not permission in failure scenario.
# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
def text(m):
    try:
        tmp = [str(s).lower() for s in m.dgndictation[0]._words]
        words = [parse_word(word) for word in tmp]
        Str(' '.join(words))(None)
    except AttributeError:
        return

keymap = {
    'cd': ['cd ; ls', Key('left'), Key('left'), Key('left'), Key('left')],
    'cd wild': ['cd **; ls', Key('left'), Key('left'), Key('left'), Key('left'), Key('left')],
    'cd wild [<dgndictation>]': ['cd **; ls', Key('left'), Key('left'), Key('left'), Key('left'), Key('left'), text],
    '(ls | run ellis | run alice)': 'ls\n',
    '(la | run la)': 'ls -la\n',
    'durrup': 'cd ..; ls\n',
    'go back': 'cd -\n',

    'pseudo': 'sudo ',
    'shell clear': [Key('ctrl-c'), 'clear\n'],
    'shell copy [<dgndictation>]': ['cp ', text],
    'shell copy (recursive | curse) [<dgndictation>]': ['cp -r', text],
    'shell kill': Key('ctrl-c'),
    'shell list [<dgndictation>]': ['ls ', text],
    'shell list all [<dgndictation>]': ['ls -la ', text],
    'shell make (durr | dear) [<dgndictation>]': ['mkdir ', text],
    'shell mipple [<dgndictation>]': ['mkdir -p ', text],
    'shell move [<dgndictation>]': ['mv ', text],
    'shell remove [<dgndictation>]': ['rm ', text],
    'shell remove (recursive | curse) [<dgndictation>]': ['rm -rf ', text],
    "shell enter": "ag -l | entr ",
    "shell enter to": "ag -l . ../.. | entr ",

    # make
    'make': 'make\n',
    'make run': 'make run\n',
    'make test': 'make test\n',
    'make build': 'make build\n',

    # git
    'jet [<dgndictation>]': ['git ', text],
    'jet add [<dgndictation>]': ['git add ', text],
    'jet branch': 'git br\n',
    'jet branch delete [<dgndictation>]': ['git br -D max/', text],
    'jet clone [<dgndictation>]': ['git clone ', text],
    'jet checkout master': 'git checkout master\n',
    'jet checkout max [<dgndictation>]': ['git checkout max/', text],
    'jet checkout [<dgndictation>]': ['git checkout ', text],
    'jet checkout branch [<dgndictation>]': ['git checkout -B max/', text],
    'jet commit [<dgndictation>]': ['git commit -m ""', Key('left'), text],
    'jet commit all [<dgndictation>]': ['git commit -a -m ""', Key('left'), text],
    'jet diff': 'git diff\n',
    'jet history': 'git hist\n',
    'jet merge [<dgndictation>]': ['git merge ', text],
    'jet pull [<dgndictation>]': ['git pull ', text],
    'jet pull base [<dgndictation>]': ['git pull --rebase ', text],
    'jet push [<dgndictation>]': ['git push ', text],
    'jet rebase [<dgndictation>]': ['git rebase ', text],
    'jet reset': 'git reset\n',
    'jet reset hard': 'git reset --hard\n',
    'jet stash': 'git stash\n',
    'jet status': 'git status\n',

    # Tools
    '(grep | grip)': ['grep  .', Key('left left')],
    'gripper': ['grep -r  .', Key('left left')],
    'pee socks': 'ps aux ',
    'vi': 'vi ',
}

ctx.keymap(keymap)


# module.exports = {
#   permissions: "chmod "
#   access: "chmod "
#   ownership: "chown "
#   "change own": "chown "
#   "change group": "chgrp "
#   cat: "cat "
#   chat: "cat " # dragon doesn't like the word 'cat'
#   copy: "cp "
#   "copy recursive": "cp -r "
#   move: "mv "
#   remove: "rm "
#   "remove recursive": "rm -rf "
#   "remove directory": "rmdir "
#   "make directory": "mkdir "
#   link: "ln "
#   man: "man "
#   list: "ls "
#   "list all": "ls -al "
#   ls: "ls "
#
#   "python reformat": "yapf -i "
#   "enter": "ag -l | entr "
#   "enter to": "ag -l . ../.. | entr "
# }
