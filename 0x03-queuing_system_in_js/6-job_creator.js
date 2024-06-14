import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  phoneNumber: '8138914240',
  message: 'Verification code'
}

const job = queue.create('push_notification_code', notification).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
