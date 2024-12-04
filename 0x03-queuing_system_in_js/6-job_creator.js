import kue from 'kue';

const jobData = {
  phoneNumber: '123458479',
  message: 'This is atest notification message'
};

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('notification', jobData);
job.save((err) => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);

    job.on('complete', () => {
      console.log('Notification job completed');
    });

    job.on('failed', () => {
      console.log('Notification job failed');
    });
  }
});
