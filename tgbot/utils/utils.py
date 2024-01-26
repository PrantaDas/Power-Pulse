from typing import List,Dict
import os

def check_envs_and_values(env_var_names: List[str]) -> None:
    """
    Checks if the specified environment variables are present and have non-empty values.

    Parameters:
    - env_var_names (List[str]): A list of environment variable names to be checked.

    Raises:
    - ValueError: If any of the specified environment variables is missing or has an empty value.

    Returns:
    - None: If all specified environment variables are present and have non-empty values.

    Example:
    >>> check_envs_and_values(['DATABASE_URL', 'SECRET_KEY'])
    => All the env vars are loaded
    """
    missing_vars = [env_var for env_var in env_var_names if env_var not in os.environ]
    empty_vars = [env_var for env_var in env_var_names if not os.environ.get(env_var)]

    if missing_vars:
        raise ValueError(f"Missing environment variable(s): {', '.join(missing_vars)}")

    if empty_vars:
        raise ValueError(f"Empty values for environment variable(s): {', '.join(empty_vars)}")

    print('=> All the env vars are loaded')



def format_user_info(data: Dict[str, str]) -> str:
    """
    Format user information into a string with HTML tags for rich text display.

    Parameters:
    - data (Dict[str, str]): A dictionary containing user information.

    Returns:
    - str: A formatted string with HTML tags for rich text display.

    Example:
    >>> user_data = {'accountNo': '123456', 'contactNo': '987654321', ...}
    >>> formatted_text = format_user_info(user_data)
    => Returns a formatted string ready for display in a messaging platform.
    """
    message = """
            <b>🟢 Customer &#9; Information 🟢</b>
            <b>🔢 Account No :{accountNo}</b>
            <b>📞 Contact No :{contactNo}</b>
            <b>👤 Customer Name :{customerName}</b>
            <b>🏢 Feeder Name :{feederName}</b>
            <b>🏠 Installation Address :{installationAddress}</b>
            <b>📅 Installation Date :{installationDate}</b>
            <b>🔢 Meter No :{meterNo}</b>
            <b>⚡ Phase Type :{phaseType}</b>
            <b>📅 Register Date :{registerDate}</b>
            <b>💡 Sanction Load :{sanctionLoad}</b>
            <b>💳 Tarif Solution :{tariffSolution}</b>
            <b>📋 Meter Model :{meterModel}</b>
            <b>🔌 Transformer :{transformer}</b>
            <b>📡 SD Name :{SDName}</b>
             """
    text = message.format(**data)
    return text