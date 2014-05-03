# Two Pope Saints

This is a rough version of the software I used to extract data and vizualize graphs and maps described in my blog post [What data is saying](http://bit.ly/1n8LqUj)

Basically, it referes to the event which tooke place in Rome on April the 27th.

The dataset has been built collecting data from Twitter using the streaming API and filtering messages containing the hashtag **#2popesaints** . 
It's fully availavle in csv format with the file [2pope.csv](https://raw.githubusercontent.com/uolter/DataDrivenJournalism/master/2popesaints/2pope.csv)

I used **python** with a set of libraries quite common in the data analisys field such as:
the 
- iPython notebook
- Pandas
- numpy
- scipy
- matplotlib
- nltk
- tweepy
- folium
- vincent

You can install all of them with *python package manager* (**pip**)

`pip install -r requirements.txt`

In order to use the twitter stream api you must register an application and fill in the settings.py file with the *consumer key*, *consumer secret*, *access token*, and *access secret* 

Then I used [mongodb](http://www.mongodb.com/) to store data before processing them.

Once mongodb is up and running you can start collecting data with:

`>> python reader.py`

Since the dataset is already provided in csv format just start iPython with the following options and omit the previous step.

`>> ipython notebook --pylab=inline`

Once your browser is open click on the link **2popesaints** in the notebook list.

Since the open street map visualization is created in a separate html file loaded in iframe it is also need to have an http listend showing the contents inside the directory where the code lies.

You can easily do that with the command:

`>> python -m SimpleHTTPServer`

To count and sum up the language used in the messages run the following script:

`>> python detect_lang.py`

This will take few minutes to provide the result.



[This work is licensed under a Creative Commons Attribution 2.0 Generic License.](http://creativecommons.org/licenses/by/2.0/) ![image](http://i.creativecommons.org/l/by/2.0/88x31.png)


