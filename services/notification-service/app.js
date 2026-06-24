const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

// Health endpoint
app.get('/api/v1/notification/health', (req, res) => {
  res.json({ status: 'UP', service: 'notification-service' });
});

app.listen(port, () => {
  console.log(`Notification service listening on port ${port}`);
});