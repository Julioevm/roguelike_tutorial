import tcod as libtcod


def handle_keys(key):
    # Movement keys
    key_char = chr(key.c)

    if key.vk == libtcod.KEY_UP or key.vk == libtcod.KEY_KP8:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key.vk == libtcod.KEY_KP2:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key.vk == libtcod.KEY_KP4:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key.vk == libtcod.KEY_KP6:
        return {'move': (1, 0)}
    elif key_char == 'y' or key.vk == libtcod.KEY_KP7:
        return {'move': (-1, -1)}
    elif key_char == 'u' or key.vk == libtcod.KEY_KP9:
        return {'move': (1, -1)}
    elif key_char == 'b' or key.vk == libtcod.KEY_KP1:
        return {'move': (-1, 1)}
    elif key_char == 'n' or key.vk == libtcod.KEY_KP3:
        return {'move': (1, 1)}


    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt + Enter: Toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Esc: Exit the game
        return {'exit': True}
    # No key pressed
    return{}
