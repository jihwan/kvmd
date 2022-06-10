# setup guide

설치전 필수 설치 라이브러리
```commandline
sudo pacman -S python-setuptools
sudo pacman -S python-wheel
sudo pacman -S python-pip
sudo pacman -S python-pbr
sudo pacman -S subverion
```

PKGBUILD 파일에 depends, optdepends 설치

일부는 https://github.com/jihwan/packages/ 클론을 받아서,
packages 하위에 것을 설치 하도록 한다.

단, libgpiod, avrdude-svn 는 https://aur.archlinux.org/ 에서 직접 다운로드 받아서 설치 한다.

## config 파일들...

configs/kvmd 를 /etc/kvmd 로 복사

extras 를 /usr/share/kvmd/extras 로 복사

contrib/keymaps 를 /usr/share/kvmd/keymaps 로 복사

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