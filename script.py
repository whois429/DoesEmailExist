import asyncio
from multiprocessing.dummy import Pool
from validate_email_address import validate_email


COUNT_OF_PROCESSES: int = 4
EMAILS_FILE_NAME: str = "emails.txt"


def get_emails() -> list[str]:
    """Gets email addresses from the file"""
    with open(EMAILS_FILE_NAME, "r") as file:
        return [line.strip() for line in file]


async def check_email(email: str) -> None:
    """Checks email"""
    if not validate_email(email, verify=True):
        print(f"{email} not valid!")


def wrapper(email: str) -> None:
    """Wrapper to run the 'check_email' function asynchronously"""
    asyncio.run(check_email(email))


if __name__ == "__main__":
    emails = get_emails()

    with Pool(processes=COUNT_OF_PROCESSES) as executor:
        executor.map(wrapper, emails)
