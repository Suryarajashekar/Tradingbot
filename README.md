# Tradingbot
A Python-based trading bot for Binance Futures Testnet that allows users to place BUY and SELL MARKET/LIMIT orders through a command-line interface. The project demonstrates modular software design, API integration, input validation, logging, and error handling for reliable automated trading operations.


# Binance Futures Testnet Trading Bot

Python CLI trading bot that places BUY/SELL orders on Binance Futures Testnet.

## Features

- MARKET orders
- LIMIT orders
- STOP orders
- BUY / SELL support
- Interactive CLI
- Logging
- Validation
- Modular architecture

## Setup

Install dependencies

pip install -r requirements.txt

Create .env file

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run

python cli.py

## Logs

All API requests and responses are stored in:

bot.log
