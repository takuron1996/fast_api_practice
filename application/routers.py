"""ルーター用モジュール."""


from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

import crud
from config.config import get_async_session
from schemas.customer import CustomerModel, CustomerResponse

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
