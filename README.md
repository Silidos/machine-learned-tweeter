This application can be used to get tweets, run the tweets through a machine learning model, and then set it up to have tweets automatically scheduled through the Google Cloud Platform. The program chooses a random line from the tweets that are produced by the bot, and tweets the line at a time depending on the schedule you have chosen. You may tweak this program to have tweets automatically scheduled through something locally such as the Windows Task Scheduler, or another cloud platform of your choosing.

Steps: 
1. Run the download_tweets.py file with the argument of the twitter user's username to download their tweets. This will be your dataset for the machine. 
2. Run the dataset through a model of your choosing, and keep the text file it produces for use on the automated tweet bot.
3. Configure config.py to have the correct name of the text file it has produced (make sure you put the text file in this same directory)
4. Edit main.py to have the correct API authentication keys to the account you want to schedule the tweets to.
5. When main.py and config.py are correctly configured, and you want to set up automatic tweets through the Google Cloud Platform, follow the remaining steps. Otherwise, edit the program as you see fit for the platform you want to automate your tweets from.
6. If you have not installed the Google Cloud SDK, you will need to do that, and you can download it here: https://cloud.google.com/sdk/downloads
7. Execute this line of code in your terminal:
 gcloud functions deploy [FUNCTION_NAME] --entry-point main --runtime python37 --trigger-resource [TOPIC_NAME] --trigger-event google.pubsub.topic.publish --timeout 540s 
This line will create the Google Cloud Function, and name the FUNCTION_NAME and the TOPIC_NAME as you see fit.
8. Execute this line of code in your terminal:
gcloud scheduler jobs create pubsub [JOB_NAME] --schedule [SCHEDULE] --topic [TOPIC_NAME] --message-body [MESSAGE_BODY]
This line will create the schedule to run the cloud function at the interval you specify. It uses Google's PubSub service, and will send a message to that service at the schedule specified. You can specify any JOB_NAME. For the schedule, it needs to be specified in the cron time format. FOr the topic name, it needs to be the same topic as the one you entered in the terminal command on step 7. The message body can be anything you see fit.
9. After these steps are finished, your tweets should be scheduled for the schedule you specified! You can run the function manually by going to the Cloud Scheduler section of the GCP console.