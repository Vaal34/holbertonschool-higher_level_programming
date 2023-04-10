#!/usr/bin/node

const x = Number(process.argv[2]);

if (x === undefined || isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x < 0) {
  // pass // use '// pass' for do nothing
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X'); // use this for don't jump on another line
    }
    console.log();
  }
}
