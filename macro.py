import logging

from talon.voice import Context, Key, talon, ContextGroup, Str


recorded_actions = []
macro_group = None

def execute_action(action, m):
    if isinstance(action, Key):
        action(m)
    else:
        Str(action)(m)

def wrap(action):
    global recorded_actions

    def wrapper(m):
        recorded_actions.append((action, m))
        logging.info(str(recorded_actions))
        execute_action(action, m)
    return wrapper

def macro_stop(m):
    global recorded_actions
    global macro_group

    print('recorded_actions', recorded_actions)
    talon.enable()
    macro_group.disable()
    macro_group.unload()

def macro_play(m):
    global recorded_actions

    for action, m in recorded_actions:
        execute_action(action, m)

def macro_start(m):
    try:
        global macro_group

        logging.info('macro_start')

        macro_group = ContextGroup('macro')
        for context_name, context in talon.subs.items():
            c = Context('copy_'+context_name, group=macro_group)
            keymap = {}
            for trigger, name in context.triggers.items():
                keymap[trigger] = wrap(context.mapping[name])
            c.keymap(keymap)

        c = Context('macro_control', group=macro_group)
        c.keymap({'macro stop': macro_stop})

        macro_group.load()
        talon.disable()
        macro_group.enable()
    except:
        macro_group.disable()
        talon.enable()

ctx = Context('macro')
ctx.keymap({
    'macro start': macro_start,
    'macro play': macro_play,
})
