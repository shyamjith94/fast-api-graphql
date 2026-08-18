import strawberry

from .user_query.user import UserQuery


@strawberry.type
class Query(
    UserQuery

):
    pass