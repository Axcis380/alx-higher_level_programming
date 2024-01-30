#!/usr/bin/env node

const fs = require('fs');

const file = process.argv[2];

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    process.stdout.write(data);
  }
});
