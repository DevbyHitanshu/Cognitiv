**Dictionary for the About:**
Keywords- Words that are thought of as a patient-important memory. Like, Name, Address, Phone number
Answers - Answers to important questions like what is your name or address or numbers.
Questions - Questions like what is your name, where do you live, etc.

##Product side
Our project helps people suffering from memory loss or amnesia in remembering basics things like name, address, and phone number. 
It's both a remedy and accessibility.
We have hardware ready to make a product band that can help the helper of an amnesic patient in case of some guidance if the patient forgets certain important keywords.

__**##What it does##**__
We are using a band that will remind people of their important memory keywords. And which will tell the other person if someone asks the patient about those things.
It will gradually learn from the frequency of forgetting and can be used to track progress

##Hardware side
The hardware is quite simple on a prototype scale we are using a raspberry pi, mic, and a speaker. On the industry level, we can use a chip instead of the bulky Arduino Uno. We are simply making all the connections such that we start a local server on a raspberry pi or on our industry-made product. Such that whenever a user joins in with that local server he can be directly taken to the website which can ask for some keywords and their answers stored in the databases.

## Software Side
We are using Natural language processing libraries ( Part of AI ) to tokenize words taken from our speech recognition mic and run them with our SQL database to check if it's a **keyword or answer or question**. Also, we have written text-to-speech and speech-to-text code.
