const assert = require('assert');
const calc = require('./0-calcul');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () =>  {
    it('should round and sum 4 and 5', () => {
        assert.strictEqual(calc(4, 5), 9);
    });

    it('should round and sum 1.05 and 3.5', () => {
        assert.strictEqual(calc(1.05, 3.5), 5);
    });

    it('should round and sum 2.75 and 4', () => {
        assert.strictEqual(calc(2.75, 4), 7);
    });

    it('should round and sum 3 and 9.65', () =>{
        assert.strictEqual(calc(3, 9.964), 13);
    });
});
