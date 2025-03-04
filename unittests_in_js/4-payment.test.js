const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const assert = require('assert');
const { send } = require('express/lib/response');

describe('Payment Request', () => {
    let consoleSpy;
    let stub;

    beforeEach(() => {
        stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        stub.restore();
        consoleSpy.restore();
    });

    it('should call calculateNumber with correct arguments and log the correct message', () => {
        sendPaymentRequestToApi(100, 20);

        assert(stub.calledWith('SUM', 100, 20));
        assert(consoleSpy.calledWith('The total is: 10'))
    })
});
