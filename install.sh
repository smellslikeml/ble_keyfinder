cd ~
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.50.tar.xz
tar xvf bluez-5.50.tar.xz
rm bluez-5.50.tar.xz
cd bluez-5.50
sudo apt-get update
sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
./configure
make
sudo make install
sudo cp attrib/gatttool /usr/local/bin/
sudo systemctl start bluetooth
