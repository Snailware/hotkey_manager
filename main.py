import keyboard as kb
import pyautogui as pag

PLAY_PAUSE_KEY: str = 'playpause'
VOLUME_UP_KEY: str = 'volumeup'
VOLUME_DOWN_KEY: str = 'volumedown'
NEXT_TRACK_KEY: str = 'nexttrack'

def main():

    kb.add_hotkey('f1', play_pause, suppress=True, trigger_on_release=True)
    kb.add_hotkey('f2', volume_down, suppress=True, trigger_on_release=True)
    kb.add_hotkey('f3', volume_up, suppress=True, trigger_on_release=True)
    kb.add_hotkey('f4', next_track, suppress=True, trigger_on_release=True)
    
    print(
    """
 hotkeys activated.

       HOTKEYS
 -------------------
 f1 -> play/pause
 f2 -> volume down
 f3 -> volume up
 f4 -> next track
 
 esc -> unmap hotkeys and close program.
    """
    )

    kb.wait('esc', suppress=True, trigger_on_release=True)
    kb.remove_all_hotkeys()
    exit()

def play_pause() -> None:
    pag.press(PLAY_PAUSE_KEY)

def volume_up() -> None:
    pag.press(VOLUME_UP_KEY)

def volume_down() -> None:
    pag.press(VOLUME_DOWN_KEY)

def next_track() -> None:
    pag.press(NEXT_TRACK_KEY)

if __name__ == '__main__':
    main()