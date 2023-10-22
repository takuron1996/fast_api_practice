"""ルーター用モジュール."""

from datetime import datetime, timedelta
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import crud
from config.config import get_async_session
from config.environment import jwt_settings
from models.customer import Customer
from schemas.customer import (
    CustomerModel,
    CustomerResponse,
    LoginCustomerModel,
    LoginCustomerRespones,
)

router = APIRouter()

@router.post(
        "/customer/",
        tags=["customer"],
        response_model=CustomerResponse,
        status_code=status.HTTP_201_CREATED)
async def create_customer_api(
    customer_model: CustomerModel,
    async_session: AsyncSession = Depends(get_async_session)
    ):
    """顧客生成用API."""
    customer = await crud.create_customer(async_session, customer_model)
    return CustomerResponse(id=customer.id, name=customer.name)

@router.post(
        "/login/",
        tags=["customer"],
        response_model=LoginCustomerRespones,
        status_code=status.HTTP_200_OK)
async def login(
    login_data: LoginCustomerModel,
    async_session: AsyncSession = Depends(get_async_session)):
    """ログインAPI."""
    def authenticate_user(customer: Optional[Customer]):
        if customer is None:
            return False
        return customer.check_password(login_data.password)

    result = await async_session.execute(
        select(Customer).where(Customer.id == login_data.id))
    customer = result.scalar_one_or_none()
    if not authenticate_user(customer):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="idかpasswordが異なります.")
    min = timedelta(minutes=jwt_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + min
    access_token = jwt.encode(
        {"sub": customer.id, "exp": expire},
        jwt_settings.JWT_SECRET_KEY,
        algorithm=jwt_settings.JWT_ALGORITHM
    )
    return LoginCustomerRespones(access_token=access_token)


@router.get("/items/")
async def read_items(
    current_customer: Annotated[Customer, Depends(crud.get_current_customer)]):
    """テスト."""
    print(current_customer)
    return {"customer_name": current_customer.name}
