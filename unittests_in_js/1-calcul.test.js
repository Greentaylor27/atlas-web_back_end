const assert = require('assert');
const calc = require('./1-calcul');

describe('calculateNumber', () => {
    describe('Addition', () => {
        it('Should return 5 after rounding 2 and 3', () => {
            assert.strictEqual(calc('SUM', 2, 3), 5);
        })

        it('Should return 6 after rounding 2.4 and 4', () => {
            assert.strictEqual(calc('SUM', 2.4, 4), 6);
        })

        it('Should return 6 after rounding 2 and 4.3', () => {
            assert.strictEqual(calc('SUM', 2, 4.3), 6)
        })
    });

    describe('Subtraction', () => {
        it('Should return 4 after rounding 5 and 1', () => {
            assert.strictEqual(calc('SUBTRACT', 5, 1), 4);
        });

        it('Should return 6 after rounding 9.4 and 3', () => {
            assert.strictEqual(calc('SUBTRACT', 9.4, 3), 6);
        });

        it('Should return 3 after rounding 8 and 5.4', () => {
            assert.strictEqual(calc('SUBTRACT', 8, 5.3), 3);
        })
    });

    describe('Division', () => {
        it('Should return 2 after rounding 10 and 5', () => {
            assert.strictEqual(calc('DIVIDE', 10, 5), 2);
        });

        it('Should return 3 after rounding 9.3 and 3', () => {
            assert.strictEqual(calc('DIVIDE', 9.3, 3), 3);
        });

        it('Should return 5 after round 15.4 and 3', () => {
            assert.strictEqual(calc('DIVIDE', 15.4, 3), 5);
        });

        it('Should return Error after rounding 1 and 0', () => {
            assert.strictEqual(calc('DIVIDE', 1, 0), 'Error')
        })
    })
});
