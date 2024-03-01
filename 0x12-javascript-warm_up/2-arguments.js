#!/usr/bin/node
/* Check passed arguments to the script */
const args = process.argv
if (args.length > 3){
    console.log('Arguments found');
}
else if (args.length == 3){
    console.log('Argument found');
}
else{
    console.log('No argument');
}
