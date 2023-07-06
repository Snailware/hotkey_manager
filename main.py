import logging as log
from json import load

import keyboard as kb
import pyautogui as pag


def main():
    EXIT_KEY = 'esc'
    log.basicConfig(filename='hotkey_manager.log',
                    filemode="a",
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    level=log.ERROR)
    
    try:
        hotkey_data = None
        with open('hotkeys.json', 'r') as hotkey_file:
            hotkey_data = load(hotkey_file)
        # get and parse json data from file. 

        print(' mapping hotkeys.\n\n\tHOTKEYS\n ---------------------')
        for hotkey in hotkey_data['hotkeys']:
            key = hotkey['hotkey']
            sent_key = hotkey['sent_key']
            description = hotkey['description']
            kb.add_hotkey(hotkey=key,
                          callback=create_callback(sent_key),
                          suppress=True,
                          trigger_on_release=True)
            print(f' {key} -> {description}')
        print(f'\n {EXIT_KEY} -> unmap hotkeys and close program.')
        # remap hotkeys according to json data, and display hotkeys.

        kb.wait(hotkey=EXIT_KEY,
                suppress=True,
                trigger_on_release=True)
        kb.remove_all_hotkeys()

    except Exception as ex:
        log.exception('an error occured:')
    exit()
    # close on EXIT_KEY press.

def create_callback(sent_key: str):
    return lambda: pag.press(sent_key)

if __name__ == '__main__':
    main()