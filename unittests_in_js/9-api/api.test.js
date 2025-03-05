const { expect } = require('chai');
const request = require('request');
const localhost = 'http://localhost:7865'


describe('Index page', () => {
    it('should return status 200', (done) => {
        request(localhost, (error, response) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return the correct message when connected', (done) => {
        request(localhost, (error, response, body) => {
            expect(response.body).to.be.a('string').that.equals('Welcome to the payment system');
            done();
        });
    });

    it('should return status 200 with correct id', (done) => {
        request(localhost + '/cart/1', (error, response) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return status 404', (done) => {
        request(localhost + '/cart/hello', (error, response) => {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
