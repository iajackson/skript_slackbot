# Handover Documentation

### How The Slack Bot Works 

The slack bot functions by reading in a message from slack, from here the internals of the slackbot work as such: 

    Slackbot Confirms with user the details of what function they want to and the values they are calling it for. 

    Slackbots interpreter determines what the appropriate module is and calls it 

    The python module once called then sends the function and values to Nats in JSON format.  

After that Nats and the Skript infrastructure then does most of the heavy lifting, running the desired function with the passed parameters. Upon the function finishing the NATS passes the result back to the Slackbot for it to output in the slack channel for the User. 


## Sequence diagram

![sequence diagram](./images/sequence.png "Sequence Diagram")

## Ideas for improvement

### For those who may be working with or extending the project in the future: 
 
Current state the NLP functions via a decision tree, with the learning data in csv format. The addition of future modules will need to be accompanied by extending the csv and adding in more example queries.  

Improving the current decision tree method of natural language processing, this may be done via implementing boosting or the random forest algorithm. Furthermore, an improvement may be made to the system by scrapping the decision tree process in the form of another machine learning mechanism. 

Currently the Slackbot has to exist in its own channel otherwise it will try to parse all messages occurring in the chat. It may be desirable to improve the Slackbot so that it can exist in a slack channel in which normal conversation occurs, without the Slackbot interrupting after every message, trying to determine what function is being called. 
