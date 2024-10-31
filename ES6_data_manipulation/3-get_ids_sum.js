export default function getStudentIdsSum(arr) {
  if (!Array.isArray(arr)) {
    return 0;
  }

  const value = 0;
  return arr.reduce((accumulator, arr) => accumulator + arr.id, value);
}

