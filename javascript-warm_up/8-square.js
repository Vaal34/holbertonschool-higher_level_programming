#!/usr/bin/node

const x = process.argv[2];

if (x === undefined) {
  console.log('Missing number of occurrences');
} else if (x < 0) {
  // pass // use '// pass' for do nothing
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('x'); // use this for don't jump on another line
    }
    console.log();
  }
}
