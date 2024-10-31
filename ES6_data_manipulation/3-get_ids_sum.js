export default function getStudentIdsSum(arr) {
  if (!Array.isArray(arr)) {
    return [];
  }

  const value = 0;
  return newArr.reduce((accumulator, arr) => accumulator + arr.id, value);
}

