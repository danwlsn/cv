#!/usr/bin/env bash
set -e

DIR=$(git rev-parse --show-toplevel)
DATE_STRING=$(date +%Y%m%d)
BUILD_FILE="build/cv-${DATE_STRING}.pdf"

pushd "$DIR/pdf"
echo "Building resume"
cp ../cv.yaml ./ 
docker run --rm -v $(pwd):/home/yamlresume yamlresume/yamlresume build cv.yaml 

echo "Copying resume"
rm cv-latest.pdf
cp cv.pdf $BUILD_FILE
cp cv.pdf cv-latest.pdf

echo "Cleaning up"
rm cv.aux cv.log cv.out cv.pdf cv.tex cv.yaml

echo "Done"
