export default class Building {
  constructor(sqft){
    if (sqft === 'number' || sqft >= 0) {
      this._sqft = sqft;
    } else {
      throw new Error('sqft must be a valid number');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (sqft !== 'number' || newSqft <= 0) {
      throw new Error('newSqft must be a valid number');
    }
    this._sqft = newSqft;
  }


}
