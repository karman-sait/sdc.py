Step 1. Environment Setup on Windows
A. Install Python and VS Code
Download Python 3.x from python.org and install it.
Download Visual Studio Code from code.visualstudio.com and install it.
In VS Code, install the Python extension for code editing and debugging.
B. Create and Activate a Virtual Environment
Open a terminal in your project folder and run:

sh
Copy
python -m venv venv
Activate the environment:

CMD/PowerShell:
sh
Copy
venv\Scripts\activate
Git Bash:
sh
Copy
source venv/Scripts/activate
C. Install Dependencies
Within the activated virtual environment, install dependencies:

sh
Copy
pip install -r requirements.txt
These dependencies include libraries for GPIO, I2C, PWM, and LED control (the real ones will be used when on Raspberry Pi).

Step 2. Setting Up QEMU to Emulate a Raspberry Pi
A. Download and Install QEMU for Windows
Download QEMU from qemu.weilnetz.de and install it on your Windows machine.
Add the QEMU installation directory to your system PATH.
B. Download Raspberry Pi OS Image
Download a Raspberry Pi OS image (for example, the 64-bit Lite version) from Raspberry Pi Downloads.

C. Create a Virtual Hard Disk for Persistence
Open a terminal (or use QEMU’s command prompt) and run:

sh
Copy
qemu-img create -f qcow2 raspios.qcow2 10G
D. Boot Raspberry Pi OS in QEMU
Use a command like the following (adjust parameters as needed):

sh
Copy
qemu-system-aarch64 -M raspi3 -cpu cortex-a72 -m 1024 \
  -drive file=raspios.qcow2,format=qcow2 \
  -dtb versatile-pb.dtb -kernel kernel8.img \
  -append "root=/dev/sda2 rw console=serial0,115200" \
  -serial stdio -net nic -net user
This boots a QEMU-emulated Raspberry Pi OS. You may need to adjust paths and filenames based on your downloaded image.

E. Set an Environment Variable in QEMU (Optional)
To help your code detect the emulated environment, you can export an environment variable inside QEMU:

sh
Copy
export QEMU_EMULATED=1
Tip: Although our code uses sys.platform to decide between mocks and real libraries, you can add additional checks if desired.

Step 3. Developing and Testing on QEMU
Open VS Code on Windows and edit your project.

Run your code locally (on Windows) with:

sh
Copy
python src/main.py
Since you’re on Windows, the mock implementations (printing messages and returning dummy sensor data) will let you test the logic.

You can also copy your project into the QEMU Raspberry Pi OS instance (using shared folders or SCP) to test with an environment closer to real hardware.

Step 4. Deploying and Testing on the Real Car
Once your code works well in your development environment:

A. Transfer the Project to Your Raspberry Pi
Use SCP (from Windows or QEMU) to copy the project:

sh
Copy
scp -r ELEGOO-Smart-Robot-Car-Kit-V4.0 pi@<raspberrypi_ip>:/home/pi/
SSH into your Raspberry Pi:

sh
Copy
ssh pi@<raspberrypi_ip>
B. Install Dependencies on the Raspberry Pi
Inside your Raspberry Pi terminal:

sh
Copy
cd /home/pi/ELEGOO-Smart-Robot-Car-Kit-V4.0
pip3 install -r requirements.txt
C. Run the Project on the Real Hardware
Make sure all wiring (motors, sensors, IR receiver, and LED strip) is connected correctly, then run:

sh
Copy
python3 src/main.py
Monitor the output and behavior. If something doesn’t work as expected (for example, sensor values or motor control), check your wiring and verify that the GPIO pin numbers in your code match your physical connections.

Step 5. Debugging and Iteration
In QEMU: Use the mock outputs (printed messages) to debug your high‑level logic.

On Real Hardware: Use print statements and logging to monitor sensor readings and control outputs.

Validate I2C connections with:

sh
Copy
i2cdetect -y 1
Verify that the libraries (e.g., pigpio, RPi.GPIO) are installed and running.

Adjust the code and wiring as needed.
