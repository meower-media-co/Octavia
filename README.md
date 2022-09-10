# Octavia
The not-so-friendly chatbot, a Meower port of Octavia! from Scratch. Also a template for Python bots.

> **Warning**
>
> Octavia will not work on the current Meower server as Meower has not been upgraded to use Cloudlink 4. Please visit [this branch](https://github.com/meower-media-co/Meower-Server/tree/main-cl4-port) for updates.

## Chat with Octavia
Simply @Octavia in Meower's home page and Octavia will respond!

> **Note**
>
> You can say hello to Octavia's [original incarnation](https://scratch.mit.edu/projects/402821371/) on Scratch.

## Making your own responses
If Octavia doesn't know how to respond to a question, she will ask you to input a response or you can tell Octavia "nevermind". You can add any kind of message response. There are some extra features you can add to a response.

> Hello, [username]!

Adding "[username]" to a response will add the origin username.

> I have stored [size] responses in my brain!

Adding [size] will return the total count of all responses in TinyDB.

## Setup
Before creating your own bot using Octavia's source code, you will need to create an account dedicated to your bot. Simply create an account from any Meower client and store the username and password of the bot in main.py.

Before you use your bot, you must install dependencies. This bot is bundled with Cloudlink 4.
`python3 -m pip install -r requirements.txt`

To run your bot, simply use
`python3 main.py`
and Octavia will connect to Meower and start listening for requests.

## Future improvements
* ~~Add a real natural-language AI~~ Outside of scope of original project idea.
* ~~Add options to use different databases other than TinyDB~~ Will likely use MongoDB in the future.
* Add feature to allow talking to Octavia in Meower chats/DMs.
* Add per-message custom PFPs to show Octavia's expressions. *(Will not be implemented until Meower B6)*

## License
Octavia is licensed using Meower's [MEOW License.](https://github.com/meower-media-co/Octavia/blob/main/LICENSE) You are completely free to use this source code in any way, shape, or form, with or without credit, for commerical or personal use. You are also free to change, remove, or keep this license. **Absolutely no patent use is permitted.**
