const assert = require('assert');
const calc = require('./0-calcul');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () =>  {
    it('should round and sum 2.75 and 4', () => {
        assert.strictEqual(calc(2.75, 4), 6); // first number being rounded
    });

    it('should round and sum 3 and 9.65', () =>{
        assert.strictEqual(calc(3, 9.65), 12); // second number being rounded
    });

    it('should round and sum 1.05 and 3.5', () => {
        assert.strictEqual(calc(1.05, 3.5), 4); // both numbers being rounded
    });

    it('should round and sum 4 and 5', () => {
        assert.strictEqual(calc(4, 5), 9); // no numbers being rounded
    });

    it('should round and sum -1 and 2', () =>{
        assert.strictEqual(calc(-1, 2), 1); // no number rounding but first number is negative
    });

    it('should round and sum 1 and -2', () =>{
        assert.strictEqual(calc(1, -2), -1); // no rounding second number is negative
    });

    it('should round and sum 1 and -1.5', () =>{
        assert.strictEqual(calc(1, -1.5), -1); // second number needs rounding and is negative 
    });

    it('should round and sum -1 and 1.5', () =>{
        assert.strictEqual(calc(-1.5, 1), -1); // first number needs rounding and is negative
    });
});
