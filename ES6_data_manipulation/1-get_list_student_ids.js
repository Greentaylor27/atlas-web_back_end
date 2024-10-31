export default function getListStudentIds(newArr) {
  if (!Array.isArray(newArr)) {
    return [];
  }
  return newArr.map((arr) => arr.id);
}
