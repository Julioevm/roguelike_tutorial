import tcod as libtcod

def handle_keys(key):
    # Movement keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (0, 1)}

    