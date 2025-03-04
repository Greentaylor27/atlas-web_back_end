const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () =>  {
    it('Should return 1 after rounding and summing 1.1 and 0', () => {
        assert.strictEqual(calculateNumber(1.1, 0), 1); // first number being rounded
    });

    it('Should return 1 after rounding and summing 0 and 1.1', () => {
        assert.strictEqual(calculateNumber(0, 1.1), 1); // first number being rounded
    });
});
