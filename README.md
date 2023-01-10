
  

# Welcome to mini_gps

  

  

Goals to reverse engineer Orginal App that comes with Leo Mini Precision GPS Reference Clock .

  

![enter image description here](http://www.leobodnar.com/shop/images/miniGPSclock-3.jpg)

  

  

**ToDo**

  

- [x] QT5 GUI

  

- [x] python3 _ core functionality

  

- [x] implementation for update Button

  

- [x] implementation for Set frequency Button (need improvement)

  

- [ ] implementation for Factory defaults Button

  

- [ ] testing in ALL OSs

	- [x] Linux

	- [ ] Windows

	- [ ] mac_os

- [ ] fix known issues

  

  

## known issues

     
  1.  > Set frequency not ideal solution (need formulas to calculate eg. N2_LS , NC1_LS and GPS_REFRENCE )
    
  2.   > usb.core.USBError: [Errno 13] Access denied (insufficient permissions) (FIX add udev rule and Disconnect and re-connect the
    USB device)

  
  

## python packages

    $  sudo apt-get install python3-pyqt5.qtsvg

    $  pip install -r requirements.txt

  

- pyqt5

  

- pyusb
- PythonQwt
  

  

## setup

  

  

**add udev rule to /etc/udev/rules.d/50-myusb.rules**

    $  sudo echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="1dd2",  ATTRS{idProduct}=="2211", GROUP="users", MODE="0666"' >> /etc/udev/rules.d/50-myusb.rules

    $  sudo udevadm control --reload-rules && sudo udevadm trigger



## TO-DO

 - [ ] Set frequency
 - [ ] impl Position and utc
 - [ ] satellite status
