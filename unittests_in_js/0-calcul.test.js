const assert = require('assert');
const calc = require('./0-calcul');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () =>  {
    it('should round and sum 2.75 and 4', () => {
        assert.strictEqual(calc(2.75, 4), 7); // first number being rounded
    });
});
