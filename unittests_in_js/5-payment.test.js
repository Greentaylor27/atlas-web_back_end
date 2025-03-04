const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const assert = require('assert');

describe('Payment Request', () => {
    let consoleSpy;
    let stub;
    
    beforeEach(() => {
        stub = sinon.stub(Utils, 'calculateNumber').callsFake((type, a, b) => {
            if (type === 'SUM') {
                return Math.round(a) + Math.round(b);
            }
            return 0;
        });

        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        stub.restore();
        consoleSpy.restore();
    });

    it('should call calculateNumber with correct arguments and log the correct message for 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);

        assert(stub.calledWith('SUM', 100, 20));
        assert(consoleSpy.calledWith('The total is: 120'));
        assert(consoleSpy.calledOnce);
    });

    it('should call calculateNumber with correct arguments and log the correct message for 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);

        assert(stub.calledWith('SUM', 10, 10));
        assert(consoleSpy.calledWith('The total is: 20'));
        assert(consoleSpy.calledOnce);
    });
});
