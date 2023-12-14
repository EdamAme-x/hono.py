from honopy import Hono

app = Hono()

def index(ctx):
  return ctx.json(app, {
    "text": "Hello world!"
  })

def name(ctx):
  return ctx.text(app, "Your name: " + ctx.params.name, {
    "status": 200
})

app.get({
  "path": "/",
  "handler": index
})

app.pos({
  "path": "/api/v1/:name",
  "handler": name
})

app.fire()
