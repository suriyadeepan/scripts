sudo add-apt-repository ppa:webupd8team/java && sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo echo 'JAVA_HOME="/usr/lib/jvm/java-8-oracle"' >> /etc/environment
echo '>> Run this $source /etc/environment'
echo '>> check $JAVA_HOME'
