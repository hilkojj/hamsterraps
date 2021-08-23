
## Install guide

- ### Install `Raspberry Pi OS Lite (32-bit)` with SSH enabled.
  With i.e. Raspi Card Imager for Android. Available in Play Store.

- ### Edit password with `passwd`

- ### Edit `/etc/wpa_supplicant/wpa_supplicant.conf` to enter WiFi network and password.
  Add `network={
        ssid="Wifi name"
        psk="Wifi password"
  }` to end of file.

- ### Execute `hostname -I` to check assigned IP adress

- ### Edit the hostname of the raspberry using `sudo raspi-config`. 
  `System options` -> `Hostname`

- Login to raspberry via SSH using `ssh pi@`*`hostname`*

