''' Object Detection

Author: Igor Souza
Email: igormcsouza@gmail.com

How to use it

...
'''

import sys

if __name__ == '__main__':
    # Test mode
    if sys.argv[1] == 'test':
        print("It's working properly!!")
    if sys.argv[1] == 'gpus':
        ## Test if GPUS are available and if tf is taking long to start up!
        from tensorflow.python.client import device_lib

        def get_available_gpus():
            local_device_protos = device_lib.list_local_devices()
            return [x.name for x in local_device_protos if x.device_type == 'GPU']

        print(get_available_gpus())