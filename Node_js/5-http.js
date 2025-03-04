const http = require('http');
const path = process.argv[2];
const count = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
    if (!path) {
        res.writeHead(404);
        res.end('Not found');
    }
    else if (req.url === '/') {
        res.end('Hello Holberton School!');
    }
    else if (req.url === '/students') {
        process.stdout.write("This is the list of out students");
        try {
            const result = await count(path);
            res.writeHead(200, { 'content-type': 'text/plain' });
            res.write('This is the list of our students\n');
            res.end(result);
        }
        catch (error) {
            res.writeHead(500);
            res.end('Error')
        }
    }
}).listen(1245);

console.log('Listening on port: 1245')

module.exports = app;
