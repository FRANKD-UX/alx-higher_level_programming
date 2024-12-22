#!/usr/bin/node
const fs = require('fs');

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destPath = process.argv[4];

const file1Content = fs.readFileSync(file1Path, 'utf8');
const file2Content = fs.readFileSync(file2Path, 'utf8');

const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destPath, concatenatedContent);
