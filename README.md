# Octavia
The not-so-friendly chatbot, a Meower port of Octavia! from Scratch. Also a template for Python bots.

## Chat with Octavia
Simply @Octavia in Meower's home page and Octavia will respond!

## Making your own responses
If Octavia doesn't know how to respond to a question, she will ask you to input a response or you can tell Octavia "nevermind". You can add any kind of message response. There are some extra features you can add to a response.

> Hello, [username]!

Adding "[username]" to a response will add the origin username.

> I have stored [size] responses in my brain!

Adding [size] will return the total count of all responses in TinyDB.

## Setup
Before creating your own bot using Octavia's source code, you will need to create an account dedicated to your bot. Simply create an account from any Meower client and store the username and password of the bot in main.py.

To run your bot, simply use
> python3 main.py
and Octavia will connect to Meower and start listening for requests.

## Future improvements
* Add a real natural-language AI
* Add options to use different databases other than TinyDB
