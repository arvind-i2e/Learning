let str = "Universe";
console.log(str, str.length);
// for(let i=0;i<str.length;i++){
//     console.log(str[i]);
// }
//For off loop works for strings
for (const char of str) {
  console.log(char);
}
//For each loop doesn't work for strings.
