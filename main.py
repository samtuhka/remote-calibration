import zmq, msgpack, time
import sys
import os
import marker_display


#convenience functions
def send_recv_notification(n):
    # REQ REP requirese lock step communication with multipart msg (topic,msgpack_encoded dict)
    req.send_multipart(('notify.%s'%n['subject'], msgpack.dumps(n)))
    return req.recv()

def get_pupil_timestamp():
    req.send('t') #see Pupil Remote Plugin for details
    return float(req.recv())


if __name__ == '__main__':

    ctx = zmq.Context()
    req = ctx.socket(zmq.REQ)
    req.connect('tcp://0.0.0.0:50020')

    def notify(notification):
            """Sends ``notification`` to Pupil Remote"""
            topic = 'notify.' + notification['subject']
            payload = msgpack.dumps(notification, use_bin_type=True)
            req.send_string(topic, flags=zmq.SNDMORE)
            req.send(payload)
            return req.recv_string()        
    
    t = time.time()
    req.send_string('T 0.0')
    print(req.recv_string())
    delay = time.time()-t
    print('Round trip command delay:', delay)
    with open("pupil_info.txt", "w") as text_file:
      text_file.write("Pupil timebase: %f" % (0.0))
      text_file.write("\nTimebase set at: %f" % (t))
      text_file.write("\nRoundtrip delay: %f" % (delay))

    n = {'subject':'start_plugin','name':'Manual_Marker_Calibration', 'args':{}}
    notify(n)
    n = {'subject':'calibration.should_start'}
    notify(n)
    marker_display.start()
    n = {'subject':'calibration.should_stop'}
    notify(n)
