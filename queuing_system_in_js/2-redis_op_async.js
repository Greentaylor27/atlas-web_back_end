import { createClient } from "redis";
import { promisify } from 'util';

const client = new createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
    // console.log('set')
    const setValue = await client.set(schoolName, value);
    console.log(`Reply: ${setValue}`)
}

async function displaySchoolValue(schoolName) {
    const value = await client.get(schoolName);
    console.log(value)
}

client.connect().then(() => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
});
