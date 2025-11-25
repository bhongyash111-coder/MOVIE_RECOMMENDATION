#!/bin/bash
# Railway build script to download Git LFS files

echo "Installing Git LFS..."
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install -y git-lfs

echo "Initializing Git LFS..."
git lfs install

echo "Pulling LFS files..."
git lfs pull

echo "Git LFS files downloaded successfully!"
ls -lh *.pkl *.csv
