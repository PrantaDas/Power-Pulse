# Power Pulse Bot

Power Pulse Bot is a Telegram bot designed to provide users of [DESCO](https://desco.gov.bd/) (Preapaid User), a prominent electricity provider company in Bangladesh, with convenient access to their account details and related information.

## Motivation
The motivation behind the development of Power Pulse Bot is to simplify and streamline the process for DESCO customers to access their electricity-related information. By leveraging the Telegram platform, users can effortlessly check their account details, balance, and daily usage, enhancing their overall experience with DESCO services.


## Features

- **User Information**: Retrieve and display detailed information about your DESCO account.
- **Check Balance**: View your current balance, meter number, and other relevant details.
- **Daily Usage**: Monitor your daily electricity consumption and associated costs.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required Python packages: `telebot`, `requests`, `redis`, and other dependencies (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PrantaDas/Power-Pulse.git
2. Change Directory:
    ```bash
    cd Power-Pulse
3. Install Dependencies
    ```bash
    pip install -r requirements.txt
4. Provide Bot token in `config.py` file:
    ```bash
    BOT_TOKEN="your_bot_token"
    DESKO_BASE_URL="http://prepaid.desco.org.bd/api"
5. Start The bot
    ```bash
    python bot.py

## Copyright and Ownership
Power Pulse Bot is developed and maintained by [Pranta Das](https://github.com/Prantadas). The bot is not affiliated with DESCO or Telegram. All rights related to DESCO's intellectual property and trademarks belong to their respective owners.

## Risks and Security
* **API Usage:** Ensure compliance with DESCO's API terms of service to avoid potential legal issues.
* **Telegram Bot Token:** Keep your Telegram bot token confidential. Unauthorized access to the token may result in misuse.
* **Data Privacy:** Be cautious about handling user data. Follow best practices to protect user privacy and comply with relevant data protection laws.
* **Third-Party Libraries:** Use reputable libraries and keep them up to date to avoid security vulnerabilities.

#### NB: 
Use this bot responsibly and adhere to ethical development practices.


Made with ❤️ by [Pranta Das](https://github.com/Prantadas)