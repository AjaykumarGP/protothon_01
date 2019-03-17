from pynput.keyboard import Key, Listener

def on_press(key):
    key=str(key)
    print('{0} '.format(
    key.upper()))




    
with Listener(on_press=on_press) as listener:
    listener.join()