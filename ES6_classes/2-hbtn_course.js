export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a valid string!');
    } else {
      this._name = name;
    }
    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a valid number');
    } else {
      this._length = length;
    }
    if (!Array.isArray(students)) {
      throw new Error('invalid students: must be array');
    } else {
      this._students = students;
    }
  }

  // getters
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new Error('newName must be a valid string');
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number' || newLength <= 0) {
      this._length = newLength;
    } else {
      throw new Error('newLength must be a valid number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents)) {
      this._students = newStudents;
    } else {
      throw new Error('newStudent must be of an array');
    }
  }
}
