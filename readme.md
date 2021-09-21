## EEG Websockets 

This app should provide a feed of alpha/theta ratios to a websocket.

The ratios are calculated in realtime from a csv file of EEG readings using a multi-taper method to calculate an average

Most of the lifting is done by the producer.

Currently timing is off as need to set an accurate frequency/socket value rather than a sleep timer.
