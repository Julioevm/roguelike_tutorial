import tcod as libtcod

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)
    
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'libtcord tutorial revised', False)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # Read input
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS,key,mouse)

        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        # Draw screen
        libtcod.console_flush()

        key = libtcod.console_check_for_keypress()

        # Exit on ESC press
        if key.vk == libtcod.KEY_ESCAPE:
            return True

if __name__ == '__main__':
    main()
