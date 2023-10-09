"""CRUDのUtils."""

from sqlalchemy.ext.asyncio import AsyncSession

from models.customer import Customer
from schemas.customer import CustomerModel


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
