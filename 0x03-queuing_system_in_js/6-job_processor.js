import { createQueue } from 'kue';

const queue = createQueue();

function sendNotification(phoneNumber, message) { 
  console.log(`sending notification to ${phoneNumber} with the message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
