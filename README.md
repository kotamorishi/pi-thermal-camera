# Raspberry Pi thermal camera

Raspberry pi thermal camera using Adafruit_AMG88xx lib.

# Adafruit libraries
Some libraries are marked as deprecated - however it still works fine.

* AMG88xx (https://github.com/adafruit/Adafruit_AMG88xx_python)
* PureIO (https://github.com/adafruit/Adafruit_Python_PureIO)
* Bitfield (https://github.com/adafruit/Adafruit_bitfield_python)
* GPIO (https://github.com/adafruit/Adafruit_Python_GPIO)

# How to run
Clone this repo
```bash
git clone https://github.com/kotamorishi/pi-thermal-camera
```

Install some libraries.
```bash
cd pi-thermal-camera
./install.sh
```

Run
```bash
python3 thermal_cam.py
```

# Ta-da
![Image of sample](https://github.com/kotamorishi/pi-thermal-camera/blob/main/images/1.jpg?raw=true)
