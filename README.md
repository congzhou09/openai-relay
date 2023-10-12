### overview

●Used to relay openai requests to https://api.openai.com, and relay back openai responses from it.

### design

◇Use Flask service to listen to all requests to it, and parse input parameters. Then send new requests using the "requests" module, and parse the returned data. Finally, respond with Flask.Response.

### reasons of some code details & tips

#### non-stream

●The request terminal will get an "Error communicating with OpenAI: ('Connection broken: InvalidChunkLength(got length b\'...', 0 bytes read" error, if all openai response headers are set into Flask.Response. So headers are not set.

#### stream

◆Openai response headers need to be set into Flask.Response. Meanwhile, header fields in Flask.Response like 'Server', 'Date', 'Connection' are not set manually, because they cannot be overwritted and will lead to "duplicated header names" error.

◆The request terminal will get an 502 status if using an remote ip address. Using domains will be OK.
