const assert = require('assert');
const calc = require('./0-calcul');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () =>  {
    it('Should return 7 after rounding and summing 2.75 and 4', () => {
        assert.strictEqual(calc(2.75, 4), 7); // first number being rounded
    });
});
