#!/usr/bin/node
/* print Multi languages with loop */

const strs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const str in strs) {
  console.log(strs[str]);
}
