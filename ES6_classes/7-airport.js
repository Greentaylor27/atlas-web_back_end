export default class Airport {
  constructor (name, code) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a valid string');
    }
    if (typeof code !== 'string') {
      throw new Error('Code must be a valid string');
    }
    this._name = name;
    this._code = code;
  }

  static toString() {
    return `[object ${this._code}]`;
  }
}
