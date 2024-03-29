
# Install guide

## Basic configuration

- Install `Raspberry Pi OS Lite (32-bit)` with SSH enabled.
  With i.e. Raspi Card Imager for Android. Available in Play Store.

- Edit password with `passwd`

- Edit `/etc/wpa_supplicant/wpa_supplicant.conf` to enter WiFi network and password.
  Add the following to the end of the file:
  ```bash
  network={
        ssid="Wifi name"
        psk="Wifi password"
  }
  ```

- Execute `hostname -I` to check assigned IP adress

- Edit the hostname of the raspberry using `sudo raspi-config`. 
  `System options` -> `Hostname`

- Login to raspberry via SSH using `ssh pi@`*`hostname`*

## Git(hub) using SSH
- Install git
- `ssh-keygen -t ed25519 -C "your_mail_adress_you_use_for_github@example.com"`
- Enter a passphrase
- `eval "$(ssh-agent -s)"`  (?)
- `ssh-add ~/.ssh/id_ed25519` (?)
- [Add the ssh key to GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). Copy and paste the contents of `~/.ssh/id_ed25519.pub`

## NGINX
- Guide from [here](https://engineerworkshop.com/blog/setup-an-nginx-reverse-proxy-on-a-raspberry-pi-or-any-other-debian-os/).
- ```bash
  sudo apt-get update
  sudo apt-get upgrade
  ```
- `sudo apt-get remove apache2` (in case apache is installed)
- `sudo apt-get install nginx`
- Confirm by browsing to `http://`*`your-hostname`*`/`
- Create `/etc/nginx/sites-available/`*`url`*`.conf`
  ```bash
  server {
    listen 4000;
    server_name *url here, e.g. raps.hilkojj.nl*;
    location / {
      proxy_pass http://localhost:8000;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "Upgrade";
    }
  }
  ```
  **NOTE**: The `Upgrade` and `Connection` headers are to support Websockets.

- `sudo ln -s /etc/nginx/sites-available/`*`url`*`.conf /etc/nginx/sites-enabled/`*`url`*`.conf`
- Confirm with `sudo nginx -t`
- Reload NGINX `sudo systemctl reload nginx`
- Read logs with
  ```
  sudo tail -f /var/log/nginx/access.log
  ```
  or
  ```
  sudo tail -f /var/log/nginx/error.log
  ```


## Firewall
- Install firewall `sudo apt install ufw`
- `sudo ufw limit 22` limited SSH access
- `sudo ufw allow 80` unlimited access to default NGINX http server (required for certbot)
- `sudo ufw allow 443` unlimited access to httpS server
- Confirm with `sudo ufw show added`
- Enable with `sudo ufw enable`
- Check status anytime with `sudo ufw status`

## Port forwarding
- Give the raspberry a static local IP adress.
- Using NAT forward port 443 from raspberry to port 443
- Using NAT forward port 80 from raspberry to port 80
- Now default NGINX server is visible on `http://`*`url`*. This is needed for certbot

## Letsencrypt (Serve over httpS)
- `sudo apt install letsencrypt`
- Confirm renewal bot is running: `sudo systemctl status certbot.timer`
- `apt install python3-certbot-nginx`
- `sudo certbot --nginx --agree-tos --preferred-challenges http -d raps.hilkojj.nl`
  
  ### NOTE:
  certbot will try to retrieve a file for confirmation from the provided url, so make sure port 80 is also port forwarded.

- Now everything that is hosted locally on port 8000 will be accessible through HTTPS (port 443): `https://`*`url`*


## Python & booting stuff

- Install Pip3 and other useful utilities:
  ```bash
  sudo apt-get install python3-dev python3-pip
  sudo python3 -m pip install --upgrade pip setuptools wheel
  ```
- Install pipenv to keep track of installed packages for this project:
  `pip3 install --user pipenv`
- Enter the environment with `pipenv shell`.

  Use `sudo -E env PATH=$PATH python boot.py` to run script with sudo
- Run boot.py on each reboot: `sudo nano /etc/crontab`.
- Add `@reboot pi cd /home/pi/hamsterraps/ && sudo -E env PATH=$PATH /home/pi/.local/bin/pipenv run sh ./boot.sh` to end of file.
  
  `sudo` is needed in order for `ws2811_init()` to succeed. (`-5` return code otherwise).

  `sudo -E env PATH=$PATH` explained [here](https://askubuntu.com/a/1342154).



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

## Waveshare display
- Add this to the end of `/boot/config.txt`:
  ```bash
  max_usb_current=1
  hdmi_group=2
  hdmi_mode=87
  hdmi_cvt 800 480 60 6 0 0 0  
  hdmi_drive=1
  ```
  [More info on waveshare display](https://www.waveshare.com/wiki/5inch_HDMI_LCD_(B))
- Enable passwordless login to console with `sudo raspi-config` -> 1 -> S5
- Follow [this](https://blog.r0b.io/post/minimal-rpi-kiosk/) (or [this](https://sylvaindurand.org/launch-chromium-in-kiosk-mode/)) guide on starting up Chromium without a window manager.
- Also don't forget to add this to `~/.bash_profile`, otherwise `~/.bashrc` and `~/.profile` won't work anymore:
  ```bash
  if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
    if [ -f "$HOME/.profile" ]; then
        . "$HOME/.profile"
    fi
  fi
  ```
- Install an emoji font with `sudo apt-get install fonts-noto-color-emoji`

## IR Camera
- Enable camera with `sudo raspi-config` and reboot
- Install ffmpeg `sudo apt install ffmpeg`

