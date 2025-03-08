#!/bin/bash

# Aiza AI Assistant setup script for Linux

echo "Setting up Aiza AI Assistant..."

# Check if SSH keys are set up
if [ ! -f ~/.ssh/id_rsa.pub ]; then
  echo "SSH keys are not set up. Setting up SSH keys..."
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
  echo "Please add the following SSH key to your GitHub account:"
  cat ~/.ssh/id_rsa.pub
  echo "Visit https://github.com/settings/keys to add your SSH key."
  read -p "Press Enter to continue after adding the SSH key to your GitHub account..."
fi

# Test SSH connection
echo "Testing SSH connection to GitHub..."
ssh -T git@github.com

if [ $? -ne 1 ]; then
  echo "SSH connection to GitHub failed. Please ensure your SSH key is added to GitHub and try again."
  exit 1
fi

# Clone the repository using SSH
echo "Cloning the repository..."
git clone git@github.com:yashraut369/Aiza.git
cd Aiza || { echo "Failed to change directory to Aiza"; exit 1; }

# Rename twilio.py to twilio_client.py to avoid conflicts
if [ -f "twilio.py" ]; then
  mv twilio.py twilio_client.py
fi

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if config.yaml exists
if [ ! -f "config.yaml" ]; then
  echo "config.yaml not found. Please create config.yaml with the required API keys."
  exit 1
fi

# Instructions for creating config.yaml
echo "Setup complete. Please ensure the 'config.yaml' file in the project root directory contains the correct API keys."

echo "To run the application, use the following command:"
echo "python main.py"

echo "Setup completed successfully."