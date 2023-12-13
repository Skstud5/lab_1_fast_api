from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return "Скрипченко Сергей"
@app.get("/tools")
async def tools_page():
    return "Я являюсь опытным программистом на Python с фокусом на веб-разработку и автоматизацию. Мой опыт включает в себя создание эффективных и масштабируемых веб-приложений, а также решение сложных задач с использованием современных технологий."

@app.get("/users")
async def users_page():
    return "Телефон: 8 800 555 35 35"