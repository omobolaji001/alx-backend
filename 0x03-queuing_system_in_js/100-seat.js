import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';


const app = express();
const port = 1245;

const queue = createQueue();
const client = createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
}).on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
const get = promisify(client.get).bind(client);

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const availableSeats = await get('available_seats');
  return availableSeats;
}

let reservationEnabled = true;

app.get('/available_seats', async function (req, res) {
  const seats = await getCurrentAvailableSeats();
  res.json({"numberOfAvailableSeats": seats});
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({"status": "Reservation are blocked"});
    return;
  }
  const job = queue.create('reserve_seat', {"seat": 1}).save((error) => {
    if (error) {
      res.json({"status": "Reservation failed"});
      return;
    } else {
      res.json({"status": "Reservation in process"});
      job.on("complete", () => {
        console.log(`Seat reservation job ${job.id} completed`);
      }).on("failed", (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
      });
    }
  });
});

app.get('/process', (req, res) => {
  res.json({"status": "Queue processing"});
  queue.process('reserve_seat', async function(job, done) {
    const seat = parseInt(await getCurrentAvailableSeats());
    if (seat === 0) {
      reservationEnabled = false;
      done(Error('Not enough seats available'));
    } else {
      reserveSeat(seat -1);
      done();
    }
  });
});


app.listen(port, () => {
  console.log(`app is listening on 127.0.0.1:${port}`);
});
reserveSeat(50);
