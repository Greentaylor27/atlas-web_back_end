export default class Currency {
  constructor(code, name){
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new Error('code must be of type string');
    }

    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('name must be of type string');
    }
  }

  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new Error('newName must be of type string');
    }
  }

  get code() {
    return this._code;
  }
  set code(newCode) {
    if (typeof newCode === 'string') {
      this._code = newCode;
    } else {
      throw new Error('newCode must be of type string');
    }
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
