# setup guide


etc/udev/rules.d/99-kvmd.rules
gpio permission ??
https://www.udoo.org/forum/threads/gpio-permissions-for-libgpiod-sudo-or-not.32453/


설치전 필수 설치 라이브러리
```commandline
sudo pacman -S python-setuptools
sudo pacman -S python-wheel
sudo pacman -S python-pip
sudo pacman -S python-pbr
sudo pacman -S subverion
```

PKGBUILD 파일에 depends, optdepends 설치
 sudo pacman -S ${library file name}

일부는 https://github.com/jihwan/packages/ 클론을 받아서,
packages 하위에 것을 설치 하도록 한다.
  makepkg -risc

단, libgpiod, avrdude-svn 는 https://aur.archlinux.org/ 에서 직접 다운로드 받아서 설치 한다.

## config 파일들...

configs/kvmd 를 /etc/kvmd 로 복사

extras 를 /usr/share/kvmd/extras 로 복사

contrib/keymaps 를 /usr/share/kvmd/keymaps 로 복사

## configs/os 설정

### /etc/udev/rules.d

twise 계정으로, video, gpio, hid 접근을 위한 설정임

```commandline
sudo cp configs/os/udev/twise.rules /etc/udev/rules.d/99-kvmd.rules
```

아래 내용은 https://github.com/jihwan/packages/blob/master/packages/raspberrypi-io-access/udev.rules
당 내용에서 GPIO 부분만 나의 환경에 맞추어 작성하였다.
```commandline
sudo vim /etc/udev/rules.d/95-raspberrypi-io-accsss.rules

SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'chown -R twise:users /sys/class/gpio && chmod -R 770 /sys/class/gpio; chown -R twise:users /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio; chown -R twise:users /sys$devpath && chmod -R 770 /sys$devpath; chown twise:users /dev/gpiomem; chown twise:users /dev/gpiochip* && chmod 660 /dev/gpiochip*'"
```

### /usr/lib/sysusers.d

twise 계정으로, video, gpio, hid 접근을 위한 설정임

```commandline
sudo cp configs/os/sysusers.conf /usr/lib/sysusers.d/kvmd.conf
```

아래 내용은 https://github.com/jihwan/packages/blob/master/packages/raspberrypi-io-access/sysusers.conf
당 내용을 아래 경로에 작성.
```commandline
sudo vim /usr/lib/sysusers.d/raspberrypi-io-access.conf

g spi - -
g gpio - -
```

### /usr/lib/tmpfiles.d

server가 기동 되면 SERVER socket이 아래 경로에 파일 형태로 생성되게 하기 위해서, 
/run/kvmd/kvmd.sock
```commandline
sudo install -DTm644 configs/os/tmpfiles.conf /usr/lib/tmpfiles.d/kvmd.conf
```



실행을 하다 보면,
  /run/kvmd 는 생성, 퍼미션을 준다.
	sudo mkdir /run/kvmd
	sudo chown -R twise:users /run/kvmd
  /dev/gpiochip0 퍼미션을 준다.
	sudo chmod 777 /dev/gpiochip0

## pycharm  실행 환경 설정

script path
```
/home/twise/pikvm/kvmd/scripts/runner
```

parameter
```
-c /home/twise/pikvm/kvmd/configs/kvmd/main.yaml --run
```

working directory
```
/home/twise/pikvm/kvmd
```