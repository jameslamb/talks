# httr-talk

## HTTP Basics

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) stands for "Hypertext Transfer Protocol". A **protocol** defines how two computers send information to each other.

Those computers get names based on their role in the protocol:

* "client": wants something
* "server": gives the client that thing if the client comes correct

The client asks for stuff by sending a "request" to the server.

A "request" has a few components:

* `URL`: Uniform Resource Locator, basically an address to find the server at
    - this is often a human-readable name like `https://api.github.com`, and the details of how that gets turned into the address of the "server" are outside the scope of this doc
* `method`: tells the server what "type" or request you are sending
    - here are slightly-oversimplified descriptions of the main ones:
        - `DELETE`: client wants the server to remove something
        - `GET`: client wants the server to send it something
        - `PATCH`: client wants to change something on the server
        - `POST`: client wants the server to create something, unless it already exists
        - `PUT`: clients wants the server to create something, and overwrite it if it already exists
* `headers`: additional context the server might need to do the right thing with the request
    - for example, `{"Accept": "application/text"}` says *"hey server, I am sending you a text file, not something like an image or audio file"*

There is a bunch of other stuff involved in the protocol but as a data scientist you shouldn't have to worry about them.


