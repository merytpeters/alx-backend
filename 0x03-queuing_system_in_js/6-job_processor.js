import kue from 'kue';

// Kue queue to listen to jobs
const push_notification_code = kue.createQueue();

// sendNotification function
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the queue
push_notification_code.process('notification', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message);

  // Mark job as completed
  done();
});
