#!/usr/bin/node
/* print c is fun based on passed argument */

const cIsFun = 'C is fun';
for (i = 0; i < Number(process.argv[2]); i++) {
    console.log(cIsFun);
}