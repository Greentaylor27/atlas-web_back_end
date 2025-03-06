import { createClient } from 'redis';

const key = 'HolbertonSchools'
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', () => {
    console.log(`Error loading`);
});

function setHash() {
    client.hSet(key, 'Paris', 2, (error, reply) => {
        if (error) {
            console.error(`Error setting hash: ${error.message}`);
        } else{
            console.log(`Reply: ${reply}`);
        }
    });
}

function getHash() {
    client.hGetAll(key, (error, reply) => {
        if (error) {
            console.error(`Error gathering Hash: ${error.message}`);
        } else {
            console.log(reply);
        }
    });
}

client.connect().then(() => {
    setHash();
    getHash();
    client.quit();
});
