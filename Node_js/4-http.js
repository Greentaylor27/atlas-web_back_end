const http = require('node:http');

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'content-type': 'text/plain' });
    res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
