#!/bin/bash
set -e

echo "Starting deployment preparation..."
echo "1. Validating Docker Compose..."
docker-compose config > /dev/null
echo "Docker Compose config is valid."

echo "2. Preparing Frontend for Vercel Deployment..."
cd frontend
# Check if vercel CLI is installed, otherwise advise
if ! command -v vercel &> /dev/null
then
    echo "WARNING: Vercel CLI not found. To install: npm i -g vercel"
else
    echo "Vercel CLI found."
fi

echo "=========================================================="
echo "DEPLOYMENT PAUSED: AUTHENTICATION / INFRASTRUCTURE REQUIRED"
echo "=========================================================="
echo "To proceed with actual deployment:"
echo "1. Ensure you have an NVIDIA GPU host for the backend."
echo "2. Run 'docker-compose up --build -d' on the host server."
echo "3. Run 'vercel login' and then 'vercel --prod' in the frontend directory."
echo "4. Set the NEXT_PUBLIC_API_URL in Vercel to your deployed backend URL."
exit 0
