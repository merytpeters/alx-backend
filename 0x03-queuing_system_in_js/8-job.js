import kue from 'kue';

const push_notification_code_3 = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('notification', jobData)
      .save((err) => {
        if (err) {
          console.log(`Notification job failed: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);

          job.on('complete', () => {
            console.log(`Notification job #${job.id} completed`);
          });
      
          // On job failure
          job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`);
          });
      
          // On job progress
          job.on('progress', (progress, data) => {
            console.log(`Notification job #${job.id} ${progress}% complete`);
          });
        }
      });
  });
}

module.exports = createPushNotificationsJobs
