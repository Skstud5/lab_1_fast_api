from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return {
        "message": "World___",
        "keyroot": "Приветствую!"
    }
@app.get("/tools")
async def tools_page():
    return "Страница Tools"

@app.get("/users")
async def users_page():
    return "Страница Users"