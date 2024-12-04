import kue from 'kue';

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];

const push_notification_code_2 = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    const errorMessage = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed();
    console.log(errorMessage.message);
    done(errorMessage);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    job.complete();
    // console.log(`Notification job #${job.id} completed`);

    done();
  }
}

push_notification_code_2.process('notification', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
