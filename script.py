import asyncio
from multiprocessing.dummy import Pool
from validate_email_address import validate_email


def get_emails():
    with open("emails.txt", "r") as file:
        return [line.rstrip() for line in file]


async def get_request(email):
    isvalid = validate_email(email, verify=True)
    if not isvalid:
        print(f"{email} not valid!")


def wrapper(email):
    asyncio.run(get_request(email))


if __name__ == "__main__":
    emails = get_emails()
    emails.append("somemfks3434fdsf3@rambler.ru")

    with Pool(processes=4) as executor:
        executor.map(wrapper, emails)
