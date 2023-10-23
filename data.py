from faker import Factory

fake = Factory.create()

def get_users_data(length: int):
    users = []
    for i in range(length):
        users.append({
            "id": i,
            "profile": fake.profile()
        })

    return users