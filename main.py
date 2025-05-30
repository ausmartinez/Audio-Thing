import dearpygui.dearpygui as dpg
import pyaudio

def printDevices():
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        print(f"Device {i}: {device_info['name']}")
        print(f"  Input Channels: {device_info['maxInputChannels']}")
        print(f"  Output Channels: {device_info['maxOutputChannels']}")
        print(f"  Default Sample Rate: {device_info['defaultSampleRate']} Hz")
        print("-----------------------")

def save_callback():
    print("Save Clicked")

def test_callback(sender):
    print(f"Test callback called {sender}")

channels = []
def addChannelsToWindow(dpg):
    with dpg.group(horizontal=True):    
        for i in range(5):
            with dpg.group():
                dpg.add_text(f"Channel {i}")
                dpg.add_slider_float(
                        label="Gain", 
                        vertical=True,
                        min_value=-20.0,
                        max_value=5,
                        default_value=0.0,
                        )
                dpg.add_button(label="Mute")

if __name__ == "__main__":
    p = pyaudio.PyAudio()

    dpg.create_context()
    dpg.create_viewport()
    
    with dpg.window(label="Audio Thing"):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Save", callback=test_callback)
                dpg.add_menu_item(label="Save As", callback=test_callback)
                with dpg.menu(label="Settings"):
                    dpg.add_menu_item(label="Setting 1", callback=test_callback, check=True)
                    dpg.add_menu_item(label="Setting 2", callback=test_callback)
            dpg.add_menu_item(label="Help", callback=test_callback)
            with dpg.menu(label="Widget Items"):
                dpg.add_checkbox(label="Pick Me", callback=test_callback)
                dpg.add_button(label="Press Me", callback=test_callback)
                dpg.add_color_picker(label="Color me", callback=test_callback)

                
        addChannelsToWindow(dpg)    

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    p.terminate()
