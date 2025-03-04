const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment')
const assert = require('assert');


describe('sendPaymentRequestToApi', () => {
    it('should call utils.calculateNumber with correct arguments', () => {
        const spy = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        assert(spy.calledOnceWith('SUM', 100, 20));
        spy.restore();
    });
});
