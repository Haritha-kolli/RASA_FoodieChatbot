# Chatbot for Foodie - UpGrad Case Study

## Problem Statement

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:

- City: Take the input from the customer as a text field. For example:

        Bot: In which city are you looking for restaurants?
        User: anywhere in Delhi
        
Assume that Foodie works only in Tier-1 and Tier-2 cities. We can use the current HRA classification of the cities from third-party source. Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".

- Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that.
Following is an example for the same:

        Bot: What kind of cuisine would you prefer?
                
        Chinese
        Mexican
        Italian
        American
        South Indian
        North Indian
        User: I’ll prefer Italian!

- Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

        Bot: What price range are you looking at?

        Lesser than Rs. 300
        Rs. 300 to 700
        More than 700
        User: in range of 300 to 700

While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.

Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message.

##  Solution

## System requirement

1. Python 3.7
2. Visual Studio Community Edition 2017
3. Rasa 2.0.0
4. Following Python packages are required
    - zomatopy
    - json
    - smtplib

## Rasa Installation

Please follow the below steps to complete system requirements

- Rasa

```
pip install rasa
```
 
- Install Rasa NLU and Spacy in the same command prompt:

```
pip install rasa[spacy]

python -m spacy download en_core_web_md

python -m spacy link en_core_web_md en
```

For detailed steps, please [check here](https://rasa.com/docs/rasa/installation/)

### Training the RASA 

To train Rasa NLU and Rasa Core, please execute the below commands

- Download the attached artifacts
- Open Command Prompt and change your directory to the downloaded artifact
- To train Rasa NLU

```
rasa train nlu
```

- To train Rasa Core

```
rasa train
```

### Running the Chatbot on CommandLine

- Open Command Prompt and change your directory to the downloaded artifact
- To start the chatbot server

```
rasa run actions
```

- To start chatbot server in command line

```
rasa shell
```

## Author

This chatbot has been developed by

- Haritha Kolli
