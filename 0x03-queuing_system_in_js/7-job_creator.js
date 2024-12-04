import kue from 'kue';

const push_notification_code_2 = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Loop through the jobs array
jobs.forEach((jobData) => {
  const job = push_notification_code_2.create('notification', jobData);
  
    // Save the job and handle the events
  job.save((err) => {
    if (err) {
      console.log(`Notification job failed: ${job.id}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
        
      // On job completion
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
  
      // On job failure
      job.on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      });
  
      // On job progress
      job.on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    }
  });
});
