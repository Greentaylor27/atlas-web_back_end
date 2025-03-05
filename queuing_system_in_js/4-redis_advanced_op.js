import { redis } from "kue";
import { createClient } from "redis";

const key = `HolbertonSchools`

const client = new createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
});

client.connect().then(() => {
    client.hSet(key, 'Portland', 50, redis.print);
    client.hSet(key, 'Seattle', 80, redis.print);
    client.hSet(key, 'New York', 20, redis.print);
    client.hSet(key, 'Bogota', 20, redis.print);
    client.hSet(key, 'Cali', 40, redis.print);
    client.hSet(key, 'Paris', 2, redis.print);

    client.hGetAll(key, (error, reply) => {
        if (error) {
            console.error(`Error retrieving the hash: ${error}`);
        } else {
            console.log(reply)
        }
    })
});
