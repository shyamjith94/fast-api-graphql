import strawberry


from .user_mutation.user import UserMutation


@strawberry.type
class Mutation(
    UserMutation
):
    pass
