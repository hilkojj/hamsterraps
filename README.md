
# Install guide

## Basic configuration

- ### Install `Raspberry Pi OS Lite (32-bit)` with SSH enabled.
  With i.e. Raspi Card Imager for Android. Available in Play Store.

- ### Edit password with `passwd`

- ### Edit `/etc/wpa_supplicant/wpa_supplicant.conf` to enter WiFi network and password.
  Add the following to the end of the file:
  ```bash
  network={
        ssid="Wifi name"
        psk="Wifi password"
  }
  ```

- ### Execute `hostname -I` to check assigned IP adress

- ### Edit the hostname of the raspberry using `sudo raspi-config`. 
  `System options` -> `Hostname`

- Login to raspberry via SSH using `ssh pi@`*`hostname`*

## Git(hub) using SSH
- ### Install git
- ### `ssh-keygen -t ed25519 -C "your_mail_adress_you_use_for_github@example.com"`
- ### Enter a passphrase
- ### `eval "$(ssh-agent -s)"`
- ### `ssh-add ~/.ssh/id_ed25519`
- ### [Add the ssh key to GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). Copy and paste the contents of `~/.ssh/id_ed25519.pub`

## Python & GPio stuff

- Install Pip3 and other useful utilities:
  ```bash
  sudo apt-get install python3-dev python3-pip
  sudo python3 -m pip install --upgrade pip setuptools wheel
  ```

## Temperature sensor
- `sudo pip3 install Adafruit_DHT`
- DHT11 sensor pins are: Signal, 5V, Ground
- Script uses GPIO pin 4, [4th pin on left column](https://www.etechnophiles.com/wp-content/uploads/2020/12/Raspberry-Pi-3-B-Pinout-in-detail.jpg)
- ```python
  import Adafruit_DHT
  import time
  
  DHT_SENSOR = Adafruit_DHT.DHT11
  DHT_PIN = 4
  
  while True:
      humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
      if humidity is not None and temperature is not None:
          print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
      else:
          print("Sensor failure. Check wiring.");
      time.sleep(3);
  ```
  *copied from [here](https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/)*