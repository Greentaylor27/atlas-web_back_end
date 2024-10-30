import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new Error('amount must be of type number');
    } else {
      this._amount = amount;
    }
    if (!(currency instanceof (Currency))) {
      throw new Error('currency must be a valid instance of Currency');
    } else {
      this._currency = currency;
    }
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof amount === 'number') {
      this._amount = newAmount;
    } else {
      throw new Error('new amount must be of type number');
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof (Currency))) {
      throw new Error('newCurrency must be of instance of Currency');
    } else {
      this._currency = newCurrency;
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw new Error('Amount must be a valid number');
    }
    if (typeof conversionRate !== 'number') {
      throw new Error('Conversion rate must be a valid number');
    }
    return amount * conversionRate;
  }
}
