import { createClient } from "redis";
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
});

async function displaySchoolValue(schoolName) {
    const getValue = await client.get(schoolName);
    console.log(getValue);
}

async function setNewSchool(schoolName, value) {
    const setValue = await client.set(schoolName, value);
    console.log(`Reply: ${setValue}`)
}

client.connect().then(() => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
    client.quit();
})
