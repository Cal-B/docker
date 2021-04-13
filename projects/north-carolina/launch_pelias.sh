#!/bin/sh
echo "Starting Pelias, make sure that docker daemon is running!"
pelias compose pull
echo "Dockerfile done"

echo "Starting elasticsearch..."
pelias elastic start
pelias elastic wait
pelias elastic create
echo "Elasticsearch done"

echo "Downloading sources in pelias.json..."
pelias download all
echo "Downloading sources in pelias.json done"

echo "Preparing polylines..."
pelias prepare polylines
echo "Polylines done"

echo "Preparing Pelias interpolation..."
pelias prepare interpolation
echo "Interpolation done"

echo "Preparing Pelias placeholder..."
pelias prepare placeholder
echo "Placeholder done..."

echo "Importing WhosOnFirst data..."
pelias import wof
echo "WhosOnFirst data done"

echo "Importing OpenAddress data..."
pelias import oa
echo "OpenAddress data done"

echo "Importing OpenStreetMap data..."
pelias import osm
echo "OpenStreetMap data done"

echo "Importing polylines..."
pelias import polylines
echo "Polylines done"

echo "Launching Pelias..."
pelias compose up

