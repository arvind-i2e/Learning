let Marks = {
  Rahul: 80,
  Avanish: 77,
  Divya: 88,
  Kamala: 95,
  Liz: 68,
};
const length = Object.keys(Marks).length;
const values = Object.values(Marks);
const sum = values.reduce((acc, value) => acc + value, 0);
const average = sum / values.length;
const getGrade = (marks) => {
  if (marks >= 90) {
    return "A";
  } else if (marks >= 80) {
    return "B";
  } else if (marks >= 70) {
    return "C";
  } else if (marks >= 60) {
    return "D";
  } else {
    return "F";
  }
};

for (let student in Marks) {
  let grade = getGrade(Marks[student]);
  console.log(`${student}: ${grade}`);
}
console.log(`Average:${average}`);
