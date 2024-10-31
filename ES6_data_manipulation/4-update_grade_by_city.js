export default function updateStudentGradeByCity(arr, city, newGrades) {
  return arr
  .filter((student) => student.location === city)
  .map((student) => {
    const newGrade = newGrades.find((item) => item.studentId === student.id);
    return { 
      ...student, 
      grade: newGrade ? newGrade.grade : 'N/A' 
    };
  });
}
