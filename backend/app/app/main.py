# from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware

# from app.api.api_v1.api import api_router

# app = FastAPI(
#     title=settings.PROJECT_NAME,
# )

# # app = FastAPI(
# #     title=settings.PROJECT_NAME, docs_url=None, redoc_url=None, openapi_url=None
# # )

# # Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# app.include_router(api_router, prefix=settings.API_V1_STR)


# app.include_router(users.router)

# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"]
# )

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.core.auth import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate

app = FastAPI()


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str

    class Config:
        orm_mode = True


@app.post("/token", response_model=Token)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """トークン発行"""
    user = authenticate(form.username, form.password)
    return create_tokens(user.id)


@app.get("/refresh_token/", response_model=Token)
async def refresh_token(current_user: User = Depends(get_current_user_with_refresh_token)):
    """リフレッシュトークンでトークンを再取得"""
    return create_tokens(current_user.id)


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """ログイン中のユーザーを取得"""
    return current_user