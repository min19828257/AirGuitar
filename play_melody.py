from melodyData import data_return
import time
import rtmidi
import melodyData


def melody_start(soe,data,midiout):
    if soe == 0:  #start or end
        return
    else:
            
        melody = data

        note_on = [0x90, melody, 112]
        note_off = [0x80, melody, 0]
        midiout.send_message(note_on)
        time.sleep(0.5)

        del midiout

def Setting():        
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()

    if available_ports:
        midiout.open_port(0)
    else:
        midiout.open_virtual_port("My virtual output")

    return midiout


