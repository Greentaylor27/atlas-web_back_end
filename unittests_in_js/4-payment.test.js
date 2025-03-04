const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const assert = require('assert');

describe('Payment Request', () => {
    
    it('should call calculateNumber with correct arguments and log the correct message', () => {
        let consoleSpy = sinon.spy(console, 'log');
        let stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        sendPaymentRequestToApi(100, 20);

        assert(stub.calledWith('SUM', 100, 20));
        assert(consoleSpy.calledWith('The total is: 10'));
        
        consoleSpy.restore();
        stub.restore();
    });
});
