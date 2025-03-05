const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
    it('should return a resolved promise when success is true', (done) => {
        getPaymentTokenFromAPI(true).then((result) => {
            expect(result).to.deep.equal({ data: 'Successful response from the API' });
            done();
        }).catch(done);
    });

    it('should return undefined when success is false', () => {
        const result = getPaymentTokenFromAPI(false);
        expect(result).to.be.undefined;
    });
});
