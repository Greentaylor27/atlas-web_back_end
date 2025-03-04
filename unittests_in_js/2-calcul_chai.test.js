const { expect } = require('chai');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    describe('Addition', () => {
        it('Should return 5', () => {
            expect(calculateNumber('SUM', 2, 3)).to.equal(5);
        })

        it('Should return 6 after rounding 2.4 and 4', () => {
            expect(calculateNumber('SUM', 2.4, 4)).to.equal(6);
        })

        it('Should return 6 after rounding 2 and 4.3', () => {
            expect(calculateNumber('SUM', 2, 4.3)).to.equal(6)
        })
    });

    describe('Subtraction', () => {
        it('Should return 4', () => {
            expect(calculateNumber('SUBTRACT', 5, 1)).to.equal(4);
        });

        it('Should return 6', () => {
            expect(calculateNumber('SUBTRACT', 9.4, 3)).to.equal(6);
        });

        it('Should return 3', () => {
            expect(calculateNumber('SUBTRACT', 8, 5.3)).to.equal(3);
        })
    });

    describe('Division', () => {
        it('Should return 2', () => {
            expect(calculateNumber('DIVIDE', 10, 5)).to.equal(2);
        });

        it('Should return 3', () => {
            expect(calculateNumber('DIVIDE', 9.3, 3)).to.equal(3);
        });

        it('Should return 5 after round 15.4 and 3', () => {
            expect(calculateNumber('DIVIDE', 15.4, 3)).to.equal(5);
        });

        it('Should return Error after rounding 1 and 0', () => {
            expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
        })
    })
});
