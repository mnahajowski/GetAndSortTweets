# GetAndSortTweets


##### Step 1

Install all the requirements. Also, keep your twitter developer account ready alongwith the API keys.

   - [Snscrape](https://github.com/JustAnotherArchivist/snscrape) is a scraper for social networking services (SNS). 
   - [Tweepy](https://github.com/itsayushisaxena/tweepy) is a library of Python to access Twitter API. 
   
To install both of these:

    pip3 install snscrape   

##### Step 2   
Open your terminal and copy the following command
For txt file:
```
snscrape twitter-search "#feminisme since:2021-03-01 until:2022-03-01" > scraped_tweets.txt
```

Now, you've got a txt file which contains the URL of the same tweets that you require.

##### Step 3

Copy the file that was created to the ./file directory in the cloned repository

##### Step 4
Run the attached python script with the following command

```
python main.py
```

##### Step 5


The results will be generated as a csv file in the main directory.