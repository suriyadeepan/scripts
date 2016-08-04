#################################
# installation for Ubuntu 16.04 
#		should work with Ubuntu 14.04
#################################

sudo apt-get --assume-yes install build-essential
sudo apt-get update
# BLAS → LAPACK → ATLAS → numpy → scipy 
# remove numpy and scipy
sudo apt-get remove python-numpy
sudo apt-get remove python-scipy

# Installation commands
sudo apt-get --assume-yes install gfortran
sudo apt-get --assume-yes install libopenblas-dev
sudo apt-get --assume-yes install liblapack-dev
sudo apt-get --assume-yes install libatlas-base-dev

# make sure wget is installed
sudo apt-get --assume-yes install wget

# Dependencies
#sudo apt-get --assume-yes install python-dev
#sudo apt-get --assume-yes install python-pip
sudo apt-get --assume-yes install python-nose
sudo apt-get --assume-yes install g++
sudo apt-get --assume-yes install git 

# Update pip
#sudo -H pip install pip -U

# Numpy
sudo -H pip install numpy -U
# Scipy
sudo -H pip install scipy -U
# Install Qt5 for matplotlib
sudo apt-get --assume-yes install qt5-default pyqt5-dev python-pyqt5 python3-pyqt5
# Matplotlib
sudo -H pip install matplotlib -U
# modify /usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/matplotlibrc
#	backend      : Qt5Agg
# sklearn
sudo -H pip install --upgrade sklearn
