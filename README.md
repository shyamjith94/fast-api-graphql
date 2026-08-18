# GraphQL User API Examples

## Create User

```graphql
mutation CreateUser {
  createUser(
    user: {
      name: "Shyam"
      email: "sedas@s.com"
    }
  ) {
    id
    name
    email
  }
}
```

## Get User

```graphql
query GetUser {
  getUser(id: 150) {
    id
    name
    email
    createDate
    updateDate
  }
}
```

## Get All Users

```graphql
query GetAllUsers {
  getUsers {
    id
    name
    email
    createDate
    updateDate
  }
}
```

## Delete User

```graphql
mutation DeleteUser($userId: Int!) {
  deleteUser(userId: $userId)
}
```

### Variables

```json
{
  "userId": 5
}
```
