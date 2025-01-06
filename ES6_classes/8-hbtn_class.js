export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw new Error('Size must be of type number');
    }
    if (typeof location !== 'string') {
      throw new Error('Location must be a valid string');
    }
    this._size = size;
    this._location = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
