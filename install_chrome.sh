#!/bin/bash
# Update package list and install dependencies
sudo apt update
sudo apt install -y wget apt-transport-https ca-certificates software-properties-common
echo "trying to install chrome"
# Add Google Chrome's repository
#wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
#sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Google Chrome
sudo apt update
sudo apt install -y google-chrome-stable
echo "finished to install chrome"