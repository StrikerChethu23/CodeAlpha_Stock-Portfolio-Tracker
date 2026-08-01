"""
STOCK PORTFOLIO TRACKER
A simple stock investment tracking system with file export
Author: [Your Name]
Date: [Current Date]
Internship: CodeAlpha - Python Programming
"""

import csv
import os
from datetime import datetime

# HARDCODED STOCK PRICES (as per requirement)
STOCK_PRICES = {
    "AAPL": 180.50,  # Apple Inc.
    "TSLA": 250.75,  # Tesla Inc.
    "GOOGL": 142.30,  # Alphabet (Google)
    "MSFT": 378.90,  # Microsoft
    "AMZN": 145.20,  # Amazon
    "META": 358.60,  # Meta (Facebook)
    "NVDA": 495.80,  # NVIDIA
    "JPM": 155.40,  # JPMorgan Chase
    "VTI": 245.30,  # Vanguard Total Stock Market
    "SPY": 478.60  # SPDR S&P 500 ETF
}

# Stock full names for display
STOCK_NAMES = {
    "AAPL": "Apple Inc.",
    "TSLA": "Tesla Inc.",
    "GOOGL": "Alphabet Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc.",
    "NVDA": "NVIDIA Corporation",
    "JPM": "JPMorgan Chase & Co.",
    "VTI": "Vanguard Total Stock Market ETF",
    "SPY": "SPDR S&P 500 ETF"
}


def display_available_stocks():
    """
    Display all available stocks with their prices
    """
    print("\n" + "=" * 60)
    print("📊 AVAILABLE STOCKS FOR TRADING")
    print("=" * 60)
    print(f"{'Symbol':<10} {'Company Name':<30} {'Price ($)':<10}")
    print("-" * 60)

    for symbol, price in STOCK_PRICES.items():
        name = STOCK_NAMES.get(symbol, symbol)
        print(f"{symbol:<10} {name:<30} ${price:<10.2f}")
    print("=" * 60)


def get_valid_stock_symbol():
    """
    Get valid stock symbol from user

    Returns:
        str: Valid stock symbol in uppercase
    """
    while True:
        symbol = input("\n🔤 Enter stock symbol (e.g., AAPL): ").strip().upper()

        if symbol in STOCK_PRICES:
            return symbol
        else:
            print(f"❌ '{symbol}' not found in our list.")
            print("📋 Available symbols:", ", ".join(sorted(STOCK_PRICES.keys())))
            choice = input("🔄 Try again? (yes/no): ").strip().lower()
            if choice in ['no', 'n']:
                return None


def get_positive_float(prompt):
    """
    Get a positive float value from user

    Args:
        prompt (str): Prompt message

    Returns:
        float: Positive float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("⚠️ Please enter a number greater than 0!")
        except ValueError:
            print("⚠️ Please enter a valid number!")


def get_positive_integer(prompt):
    """
    Get a positive integer from user

    Args:
        prompt (str): Prompt message

    Returns:
        int: Positive integer value
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("⚠️ Please enter a number greater than 0!")
        except ValueError:
            print("⚠️ Please enter a valid whole number!")


def input_stock_portfolio():
    """
    Get stock portfolio from user input

    Returns:
        dict: Portfolio dictionary {symbol: {'shares': X, 'buy_price': Y}}
    """
    portfolio = {}

    print("\n" + "=" * 60)
    print("📈 BUILD YOUR STOCK PORTFOLIO")
    print("=" * 60)
    print("💡 Tip: You can add multiple stocks to your portfolio")

    while True:
        # Show available stocks
        display_available_stocks()

        # Get stock symbol
        symbol = get_valid_stock_symbol()
        if symbol is None:
            break

        # Get current price
        current_price = STOCK_PRICES[symbol]
        print(f"💰 Current price of {symbol}: ${current_price:.2f}")

        # Get number of shares
        shares = get_positive_integer(f"📊 Enter number of shares of {symbol}: ")

        # Get purchase price (allow different from current price)
        print(f"💡 Tip: Current price is ${current_price:.2f}")
        buy_price = get_positive_float(f"💵 Enter purchase price per share for {symbol}: $")

        # Add to portfolio
        portfolio[symbol] = {
            'shares': shares,
            'buy_price': buy_price,
            'current_price': current_price
        }

        print(f"✅ Added {shares} shares of {symbol} at ${buy_price:.2f} each")

        # Ask if user wants to add more stocks
        more = input("\n➕ Add another stock? (yes/no): ").strip().lower()
        if more in ['no', 'n']:
            break

    return portfolio


def calculate_portfolio_summary(portfolio):
    """
    Calculate portfolio summary statistics

    Args:
        portfolio (dict): Portfolio dictionary

    Returns:
        dict: Summary statistics
    """
    total_investment = 0
    total_current_value = 0
    total_profit_loss = 0
    stocks = []

    for symbol, data in portfolio.items():
        shares = data['shares']
        buy_price = data['buy_price']
        current_price = data['current_price']

        investment = shares * buy_price
        current_value = shares * current_price
        profit_loss = current_value - investment
        profit_loss_pct = ((current_value - investment) / investment) * 100 if investment > 0 else 0

        stocks.append({
            'symbol': symbol,
            'shares': shares,
            'buy_price': buy_price,
            'current_price': current_price,
            'investment': investment,
            'current_value': current_value,
            'profit_loss': profit_loss,
            'profit_loss_pct': profit_loss_pct
        })

        total_investment += investment
        total_current_value += current_value
        total_profit_loss += profit_loss

    total_profit_loss_pct = ((
                                         total_current_value - total_investment) / total_investment) * 100 if total_investment > 0 else 0

    return {
        'stocks': stocks,
        'total_investment': total_investment,
        'total_current_value': total_current_value,
        'total_profit_loss': total_profit_loss,
        'total_profit_loss_pct': total_profit_loss_pct,
        'num_stocks': len(stocks)
    }


def display_portfolio_summary(summary):
    """
    Display portfolio summary in a formatted table

    Args:
        summary (dict): Portfolio summary
    """
    print("\n" + "=" * 80)
    print("📊 PORTFOLIO SUMMARY")
    print("=" * 80)

    # Header
    print(
        f"{'Symbol':<8} {'Shares':<8} {'Buy Price':<12} {'Current Price':<14} {'Investment':<14} {'Current Value':<16} {'P/L':<12} {'P/L %':<8}")
    print("-" * 80)

    # Stock details
    for stock in summary['stocks']:
        profit_loss = stock['profit_loss']
        profit_loss_pct = stock['profit_loss_pct']

        # Color indicators for profit/loss
        pl_indicator = "🟢" if profit_loss > 0 else "🔴" if profit_loss < 0 else "⚪"

        print(
            f"{stock['symbol']:<8} {stock['shares']:<8} ${stock['buy_price']:<11.2f} ${stock['current_price']:<13.2f} ${stock['investment']:<13.2f} ${stock['current_value']:<15.2f} {pl_indicator} ${profit_loss:<10.2f} {profit_loss_pct:>6.2f}%")

    print("-" * 80)

    # Totals
    print(f"\n📊 PORTFOLIO TOTALS:")
    print(f"   💰 Total Investment:     ${summary['total_investment']:,.2f}")
    print(f"   💵 Total Current Value:  ${summary['total_current_value']:,.2f}")

    # Show profit/loss with color indicator
    if summary['total_profit_loss'] > 0:
        print(
            f"   🟢 Total Profit/Loss:    +${summary['total_profit_loss']:,.2f} (+{summary['total_profit_loss_pct']:.2f}%)")
    elif summary['total_profit_loss'] < 0:
        print(
            f"   🔴 Total Profit/Loss:    -${abs(summary['total_profit_loss']):,.2f} ({summary['total_profit_loss_pct']:.2f}%)")
    else:
        print(f"   ⚪ Total Profit/Loss:    ${summary['total_profit_loss']:,.2f} (0.00%)")

    print(f"   📈 Number of Stocks:    {summary['num_stocks']}")
    print("=" * 80)


def export_to_csv(portfolio, summary):
    """
    Export portfolio data to CSV file

    Args:
        portfolio (dict): Portfolio dictionary
        summary (dict): Portfolio summary

    Returns:
        str: Filename of exported file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.csv"

    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Symbol', 'Shares', 'Buy Price', 'Current Price',
                          'Investment', 'Current Value', 'Profit/Loss', 'Profit/Loss %']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for stock in summary['stocks']:
                writer.writerow({
                    'Symbol': stock['symbol'],
                    'Shares': stock['shares'],
                    'Buy Price': f"${stock['buy_price']:.2f}",
                    'Current Price': f"${stock['current_price']:.2f}",
                    'Investment': f"${stock['investment']:.2f}",
                    'Current Value': f"${stock['current_value']:.2f}",
                    'Profit/Loss': f"${stock['profit_loss']:.2f}",
                    'Profit/Loss %': f"{stock['profit_loss_pct']:.2f}%"
                })

            # Add summary rows
            writer.writerow({})
            writer.writerow({'Symbol': 'TOTALS', 'Investment': f"${summary['total_investment']:.2f}",
                             'Current Value': f"${summary['total_current_value']:.2f}",
                             'Profit/Loss': f"${summary['total_profit_loss']:.2f}",
                             'Profit/Loss %': f"{summary['total_profit_loss_pct']:.2f}%"})

        print(f"\n✅ Portfolio exported successfully to: {filename}")
        return filename
    except Exception as e:
        print(f"\n❌ Error exporting to CSV: {e}")
        return None


def export_to_text(portfolio, summary):
    """
    Export portfolio data to text file

    Args:
        portfolio (dict): Portfolio dictionary
        summary (dict): Portfolio summary

    Returns:
        str: Filename of exported file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.txt"

    try:
        with open(filename, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("📊 STOCK PORTFOLIO REPORT\n")
            f.write(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            # Stock details
            f.write("STOCK HOLDINGS:\n")
            f.write("-" * 80 + "\n")
            f.write(
                f"{'Symbol':<8} {'Shares':<8} {'Buy Price':<12} {'Current Price':<14} {'Investment':<14} {'Current Value':<16} {'P/L':<12}\n")
            f.write("-" * 80 + "\n")

            for stock in summary['stocks']:
                f.write(
                    f"{stock['symbol']:<8} {stock['shares']:<8} ${stock['buy_price']:<11.2f} ${stock['current_price']:<13.2f} ${stock['investment']:<13.2f} ${stock['current_value']:<15.2f} ${stock['profit_loss']:<10.2f}\n")

            f.write("-" * 80 + "\n\n")

            # Summary
            f.write("PORTFOLIO SUMMARY:\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Investment:     ${summary['total_investment']:,.2f}\n")
            f.write(f"Total Current Value:  ${summary['total_current_value']:,.2f}\n")
            f.write(f"Total Profit/Loss:    ${summary['total_profit_loss']:,.2f}\n")
            f.write(f"Profit/Loss %:        {summary['total_profit_loss_pct']:.2f}%\n")
            f.write(f"Number of Stocks:     {summary['num_stocks']}\n")
            f.write("=" * 80 + "\n")

        print(f"\n✅ Portfolio exported successfully to: {filename}")
        return filename
    except Exception as e:
        print(f"\n❌ Error exporting to text file: {e}")
        return None


def main():
    """
    Main function to run the Stock Portfolio Tracker
    """
    print("\n" + "=" * 60)
    print("📈 STOCK PORTFOLIO TRACKER")
    print("📚 CodeAlpha Python Internship - Task 2")
    print("=" * 60)

    # Get portfolio input
    portfolio = input_stock_portfolio()

    if not portfolio:
        print("\n⚠️ No stocks added. Exiting...")
        return

    # Calculate summary
    summary = calculate_portfolio_summary(portfolio)

    # Display summary
    display_portfolio_summary(summary)

    # Ask if user wants to save results
    print("\n📁 SAVE RESULTS")
    print("1. Save as CSV")
    print("2. Save as Text File")
    print("3. Skip saving")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            export_to_csv(portfolio, summary)
            break
        elif choice == '2':
            export_to_text(portfolio, summary)
            break
        elif choice == '3':
            print("\n📂 Results not saved.")
            break
        else:
            print("⚠️ Please enter 1, 2, or 3!")

    print("\n" + "=" * 60)
    print("✅ Thank you for using the Stock Portfolio Tracker!")
    print("💼 Keep investing wisely with CodeAlpha!")
    print("=" * 60)


# Program entry point
if __name__ == "__main__":
    main()