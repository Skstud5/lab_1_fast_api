from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return {
        "FIO": "Скрипченко Сергей"
    }


@app.get("/tools")
async def tools_page():
    return {
        "description": "Я являюсь опытным программистом на Python с фокусом на веб-разработку и автоматизацию. Мой "
                       "опыт включает"
                       "в себя создание эффективных и масштабируемых веб-приложений, а также решение сложных задач с "
                       "использованием современных технологий."
    }


@app.get("/users")
async def users_page():
    return {
        "phone": "Телефон: 8 800 555 35 35"
    }
