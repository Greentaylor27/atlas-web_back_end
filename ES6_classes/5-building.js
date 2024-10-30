export default class Building {
  constructor(sqft) {
    if (sqft === 'number' || sqft >= 0) {
      this._sqft = sqft;
    } else {
      throw new Error('sqft must be a valid number');
    }
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (newSqft !== 'number' || newSqft <= 0) {
      throw new Error('newSqft must be a valid number');
    }
    this._sqft = newSqft;
  }
}
