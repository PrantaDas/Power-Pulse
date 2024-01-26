# Power Pulse Bot

Power Pulse Bot is a Telegram bot designed to provide users of DESCO (Preapaid User), a prominent electricity provider company in Bangladesh, with convenient access to their account details and related information.

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
    BOT_TOKEN=""
    DESKO_BASE_URL="http://prepaid.desco.org.bd/api"

