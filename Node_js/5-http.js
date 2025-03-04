const http = require('http');
const path = process.argv[2];
const count = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    if (!path) {
        res.writeHead(404);
        res.end('Not found');
    }
    else if (req.url === '/') {
        res.end('Hello Holberton School!');
    }
    else if (req.url === '/students') {
        console.log("This is the list of our students")
        count(path);
    }
}).listen(1245);

module.exports = app;
