users = {
    12314442: {
        'q_num': 1,
        'axes': {
            'I - E': 0,
            'S - N': 0,
            'F - T': 0,
            'J - P': 0,
        },
        'p_type': 'untitled'
    }
}


import asyncio
from sqlalchemy import create_engine, BigInteger, select
from sqlalchemy.orm import registry, declarative_base, as_declarative, mapped_column, Mapped, Session, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker, AsyncSession

engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
async_s = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class UsersTable(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    question_num: Mapped[int] = mapped_column()
    I_E: Mapped[float] = mapped_column()
    S_N: Mapped[float] = mapped_column()
    F_T: Mapped[float] = mapped_column()
    J_P: Mapped[float] = mapped_column()
    p_type: Mapped[str] = mapped_column()


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_user(async_session: async_sessionmaker[AsyncSession], user_id):
    async with async_session() as session:
        async with session.begin():
            user = UsersTable(user_id=user_id, question_num=1, I_E=0, S_N=0, F_T=0, J_P=0, p_type='untitled')
            session.add(user)


# todo: функция обновления данных


async def get_data(async_session: async_sessionmaker[AsyncSession], user_id):
    async with async_session() as session:
        async with session.begin():
            res = await session.execute(select(UsersTable).where(UsersTable.user_id == user_id))
            user = res.scalar_one_or_none()
            if user:
                return {
                    "user_id": user.user_id,
                    "I_E": user.I_E,
                    "S_N": user.S_N,
                    "F_T": user.F_T,
                    "J_P": user.J_P,
                    "p_type": user.p_type,
                }
            return None


async def main():
    """Основная асинхронная функция для тестирования."""
    await create_table()
    await add_user(async_s, 12333)
    user = await get_data(async_s, 12333)
    print(user)


# Запуск асинхронного кода
asyncio.run(main())