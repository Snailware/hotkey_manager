from json import load

import keyboard as kb
import pyautogui as pag

def main():
    EXIT_KEY = 'esc'

    hotkey_data = None
    with open('hotkeys.json', 'r') as hotkey_file:
        hotkey_data = load(hotkey_file)
    # get and parse json data from file. 

    print(' mapping hotkeys.\n\n\tHOTKEYS\n\n ------------------------')
    for hotkey in hotkey_data['hotkeys']:
        key = hotkey['hotkey']
        sent_key = hotkey['sent_key']
        kb.add_hotkey(hotkey=key,
                      callback=lambda: pag.press(sent_key),
                      suppress=True,
                      trigger_on_release=True)
        print(f' {key} -> {sent_key}')
    print(f'\n {EXIT_KEY} -> unmap hotkeys and close program.')
    # remap hotkeys according to json data, and display hotkeys.

    kb.wait(EXIT_KEY, suppress=True, trigger_on_release=True)
    kb.remove_all_hotkeys()
    exit()
    # close on EXIT_KEY press.

if __name__ == '__main__':
    main()