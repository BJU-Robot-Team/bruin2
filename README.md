# BJU Robot Team's Bruin 2 Code
The new home for Bruin 2 code

This is the Bruin 2 Robot code, converted from the old repository "Bruin-2-Master" to this new one for clarity. The code has also been transformed from a predominately C++ project to Python project, though some of the modules that are not written by the team, such as the RoboteQ driver, are still in C++. 

# Getting started
## Prerequisites
1. [VMWare](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0) or some other hypervisor, or if running natively, no hypervisor is needed
2. [Ubuntu](https://www.ubuntu.com/download/desktop) version 18.04 bionic beaver
3. [VS Code](https://code.visualstudio.com/) or some other code editor
4. git: `sudo apt install git`
5. pip: `sudo apt-get install pip`

## Setup
- Clone the repo: `cd ~ && git clone https://github.com/BJU-Robot-Team/bruin2.git bruin_2_code`
- Run `py -m virtualenv bruin2_env` to set up a virtual environment, then `pip install -r requirements.txt` to install the required modules
- Run `source ~/bruin_2_code/setup.sh` to install the dependencies (This may take up to an hour) (Is this still needed?)
- Run `catkin_make` from ~/bruin_2_code to build the code
- Run `./run_bruin2.sh` from ~/bruin_2_code to run the code


# Architecture
The Bruin-2 Robot is built on a golf cart frame with several important electronic pieces that help control it
## Electronic components
### Sensors
- GPS: connected over serial at 4800 baud
- Compass: connected over serial at 19200 baud
- Camera: connected over USB
- LIDAR: connected over USB. Not currently connected to anything

### Actuators
- [Relay Board](https://docs.numato.com/doc/16-channel-usb-relay-module/): connected over USB, with a serial-like interface. Also has GPIO pins
