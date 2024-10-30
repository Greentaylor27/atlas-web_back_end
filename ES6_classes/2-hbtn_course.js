export default class HolbertonCourse {
  constructor(name, length, students) {

    if (typeof name !== 'string'){
      throw new Error("Name must be a valid string!");
    } else {
      this._name = name;
    }
    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a valid number');
    } else {
      this._length = length;
    }
    if (!Array.isArray(students)){
      throw new Error('invalid students: must be array');
    } else {
      this._students = students;
    }
  }

  get name(){
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = newStudents;
  }

}
