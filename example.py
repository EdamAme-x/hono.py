from honopy import Hono

app = Hono()

def index(context):
  return context.json({
    "text": "Hello world!"
  })

def name(context):
  return context.text("Your name: " + context.params.name)

app.get({
  path: "/",
  handler: index
})

app.pos({
  path: "/api/v1/:name",
  handler: name
})

app.fire()
