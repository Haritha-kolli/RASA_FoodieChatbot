## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody": "del Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\nhi"}
* affirm
    - utter_ask_email
* send_email{"email":"haritha.kolli96@gmail.com"}
    - slot{"email":"haritha.kolli96@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"haritha.kolli96@gmail.com"}
    - slot{"email":"haritha.kolli96@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
     - utter_ask_price
* restaurant_search{"price":"mid"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* goodbye
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
     - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":""}
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"haritha.kolli96@gmail.com"}
    - slot{"email":"haritha.kolli96@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"haritha.kolli96@gmail.com"}
    - slot{"email":"haritha.kolli96@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":""}
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price":"mid"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"littlecaptures9@gmail.com"}
    - slot{"email":"littlecaptures9@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"haritaa.kolli@gmail.com"}
    - slot{"email":"haritaa.kolli@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price":"mid"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* goodbye
    - utter_goodbye

## happy_path_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price":"mid"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* goodbye
    - utter_goodbye

## happy_path_3
* greet
    - utter_greet
* restaurant_search{"price":"low","cuisine": "mexican", "location": "mumbai"}
    - slot{"price":"low"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* goodbye
    - utter_goodbye


## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price":"high"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* goodbye
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"price":"high","cuisine": "south indian", "location": "bengaluru"}
    - slot{"price":"high"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - slot{"emailbody":" Pizzasia in Shop 1 A, 315, Ground Floor, Ocean Complex, P Block, Pocket A, Maharaja Agrasen Marg, Sector 18, Noida has been rated 3.9\n"}
* affirm
    - utter_ask_email
* send_email{"email":"houseofiravath@gmail.com"}
    - slot{"email":"houseofiravath@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "south indian", "location": "bengaluru"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bengaluru"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " The Restaurant - Coorg in 477, Krishna Temple Road, 1st Stage, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.4\n The Permit Room in 16/3, Ram Kunj, Commissariat Road, Ashok Nagar, Opposite Garuda Mall, Brigade Road, Bangalore has been rated 4.3\n Bob's Bar in 777/I, HAL 2nd Stage, 100 Feet Road, Opposite New Horizon School, Indiranagar, Bangalore has been rated 4.1\n"}
* affirm
    - utter_ask_email
* send_email{"email": "littlecaptures9@gmail.com"}
    - slot{"email": "littlecaptures9@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"emailbody": ""}
* goodbye
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "visakhapatnam"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "visakhapatnam"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Soup Stop in Rednam Estates, Near Bank of India, 1st Lane, Opposite Ravindra Bharati School, Dwaraka Nagar, Vizag with average budget for two people Rs.750 has been rated 4.2\n Ming Garden - The Gateway Hotel in The Gateway Hotel, Beach Road, Maharani Peta, Visakhapatnam, Maharani Peta, Vizag with average budget for two people Rs.2000 has been rated 4.1\n"}
* goodbye
    - utter_goodbye

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "warangal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "warangal"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Soup Stop in Rednam Estates, Near Bank of India, 1st Lane, Opposite Ravindra Bharati School, Dwaraka Nagar, Vizag with average budget for two people Rs.750 has been rated 4.2\n Ming Garden - The Gateway Hotel in The Gateway Hotel, Beach Road, Maharani Peta, Visakhapatnam, Maharani Peta, Vizag with average budget for two people Rs.2000 has been rated 4.1\n"}
* goodbye
    - utter_goodbye

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bijapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bijapur"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Soup Stop in Rednam Estates, Near Bank of India, 1st Lane, Opposite Ravindra Bharati School, Dwaraka Nagar, Vizag with average budget for two people Rs.750 has been rated 4.2\n Ming Garden - The Gateway Hotel in The Gateway Hotel, Beach Road, Maharani Peta, Visakhapatnam, Maharani Peta, Vizag with average budget for two people Rs.2000 has been rated 4.1\n"}
* goodbye
    - utter_goodbye

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "ujjain"}
    - slot{"location": "ujjain"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "tiruvannamalai"}
    - slot{"location": "tiruvannamalai"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "thanjavur"}
    - slot{"location": "thanjavur"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika@gmail.com"}
    - slot{"email": "haritha.harika@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "priyasri1996@gmail.com"}
    - slot{"email": "priyasri1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "purulia"}
    - slot{"location": "purulia"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "haritha.harika1996@gmail.com"}
    - slot{"email": "haritha.harika1996@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "balaji98@gmail.com"}
    - slot{"email": "balaji98@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "meerut"}
    - slot{"location": "meerut"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "balaji98@gmail.com"}
    - slot{"email": "balaji98@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "noida"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": " Soup Stop in Rednam Estates, Near Bank of India, 1st Lane, Opposite Ravindra Bharati School, Dwaraka Nagar, Vizag with average budget for two people Rs.750 has been rated 4.2\n Ming Garden - The Gateway Hotel in The Gateway Hotel, Beach Road, Maharani Peta, Visakhapatnam, Maharani Peta, Vizag with average budget for two people Rs.2000 has been rated 4.1\n"}
* goodbye
    - utter_goodbye

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": " Plum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6\n Honk - Pullman New Delhi Aerocity in Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6\n You Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5\n Jom Jom Malay in S12-A, 2nd Floor, Select City Walk, Saket, New Delhi has been rated 4.5\n Yeti - The Himalayan Kitchen in T 7 A, Khirki Extension, Malviya Nagar, New Delhi has been rated 4.4\n C.I.A. Call It Asiian in 13- 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi has been rated 4.4\n Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.4\n Plum By Bent Chair in 22, Janpath Road, Janpath, New Delhi has been rated 4.4\n Nagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.3\n Pa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.2\n"}
* affirm
    - utter_ask_email
* send_email{"email": "balaji98@gmail.com"}
    - slot{"email": "balaji98@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
