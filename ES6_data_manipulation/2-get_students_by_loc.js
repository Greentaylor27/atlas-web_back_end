export default function getStudentsByLocation(newArr, city) {
  if (!Array.isArray(newArr)) {
    return [];
  }
  if (typeof city !== 'string') {
    return [];
  }

  return newArr.filter((arr) => arr.location === city);
}
