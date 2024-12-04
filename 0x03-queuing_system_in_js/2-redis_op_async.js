import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  (console.log(`Redis client not connected to the server: ${err.message}`));
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue (schoolName) {
  try {
    const value = await getAsync(schoolName);
    if (value) {
      console.log(`${value}`);
    } else {
      console.get(`${schoolName} does not exit in Redis.`);
    }
  } catch (err) {
    console.log(`Error retrieving value: ${err.message}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
