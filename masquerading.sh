#!/bin/bash
set -e

# Interfaces
WAN_IFACE="wlp0s20f3"
LAN_IFACE="enx5c857e34bd87"

echo "Enabling IP forwarding..."
sudo sysctl -w net.ipv4.ip_forward=1

echo "Making IP forwarding permanent in /etc/sysctl.conf..."
sudo sed -i '/^net.ipv4.ip_forward=/d' /etc/sysctl.conf
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf

echo "Setting up iptables masquerade rules..."
sudo iptables -t nat -A POSTROUTING -o $WAN_IFACE -j MASQUERADE
sudo iptables -A FORWARD -i $WAN_IFACE -o $LAN_IFACE -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i $LAN_IFACE -o $WAN_IFACE -j ACCEPT

echo "Saving iptables rules..."
sudo apt-get update
sudo apt-get install -y iptables-persistent
sudo netfilter-persistent save

echo "Setup complete!"
