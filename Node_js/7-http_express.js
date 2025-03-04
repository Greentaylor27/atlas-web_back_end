const express = require('express')
const count = require('./3-read_file_async')
const app = express()
const port = 1245
const path = process.argv[2]

app.get('/', (req, res) => {
    res.send('Hello Holberton School!')
});

app.get('/students', async (req, res) => {
    try {
        const studentList = await count(path);
        res.send(`This is the list of out students\n ${studentList}`);
    }
    catch {
        res.status(500).send('Error reading file')
    }
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
});

module.exports = app;
