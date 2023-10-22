"""CRUDのUtils."""

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from config.config import get_async_session
from config.environment import jwt_settings
from models.customer import Customer
from schemas.customer import CustomerModel

api_key_scheme = APIKeyHeader(name="Authorization")

async def get_current_customer(
        api_key: str = Depends(api_key_scheme),
        async_session: AsyncSession = Depends(get_async_session)):
    """ログインしている顧客を取得."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    header = api_key.split()
    if len(header) != 2:
        raise credentials_exception
    prefix, token = header
    if prefix.lower() != "bearer":
        raise credentials_exception
    try:
        payload = jwt.decode(
            token,
            jwt_settings.JWT_SECRET_KEY,
            algorithms=jwt_settings.JWT_ALGORITHM)
        customer_id = payload.get("sub")
        if customer_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    result = await async_session.execute(
        select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if customer is None:
        raise credentials_exception
    return customer


async def create_customer(
        async_session: AsyncSession,customer_model: CustomerModel
    ) -> Customer:
    """顧客を生成."""
    customer = Customer(name = customer_model.name)
    customer.set_password(customer_model.password)
    async_session.add(customer)
    await async_session.commit()
    await async_session.refresh(customer)
    return customer
