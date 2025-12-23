# Invest Vision

A comprehensive investment simulation tool that allows users to model and visualize the growth of their investments over time using historical data from Yahoo Finance. This tool demonstrates the power of compound interest with various investment strategies.

## Features

- Real-time financial data from Yahoo Finance
- Interactive investment simulation with customizable parameters
- Historical data simulation based on actual market performance
- Multiple compounding frequencies (daily, weekly, monthly, quarterly, yearly)
- Support for over 100 Indonesian stocks (IDX) and 50 global assets
- Dark/light mode with smooth transitions
- Currency support (USD, IDR, EUR)
- Visual charting of investment growth over time
- Detailed performance metrics and profit calculations

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Data Visualization**: Chart.js
- **Data Source**: Yahoo Finance API via yfinance
- **Styling**: Tailwind CSS

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/fiandev/compounding-simulation.git
   cd compounding-simulation
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. Configure your investment parameters:
   - Select an asset ticker from the comprehensive list
   - Set your initial capital and monthly top-up amount
   - Choose the compounding frequency (daily, weekly, monthly, etc.)
   - Set the investment duration (1-40 years)

4. Click "Jalankan Simulasi" to run the simulation

5. View the results including:
   - Total invested amount
   - Total profit/loss
   - Final portfolio value
   - Interactive growth chart

## API Endpoints

- `GET /` - Main application interface
- `GET /api/tickers` - Get list of available tickers
- `POST /api/simulate` - Run investment simulation

## Simulation Logic

The simulation uses historical data from Yahoo Finance to model realistic investment growth:

1. Retrieves historical price data for the selected asset
2. Calculates the Compound Annual Growth Rate (CAGR)
3. Simulates compounding based on the selected frequency
4. Accounts for regular top-up investments
5. Projects growth over the specified duration

The model takes into account actual market performance patterns, allowing users to see how their investments might have behaved historically.

## Asset Categories

### Indonesian Stocks (IDX)
- Top 100 Indonesian stocks including major banks (BBCA, BBRI, BMRI, BBNI)
- Technology companies (GOTO, AMMN)
- Mining and commodities (ADRO, ANTM, ITMG)
- Consumer goods (UNVR, ICBP, INDF)

### Global Assets
- Major technology stocks (AAPL, MSFT, GOOGL, NVDA, TSLA)
- Cryptocurrencies (BTC-USD, ETH-USD)
- Commodities (Gold, Silver)
- International blue-chip stocks

## Customization Options

- Multiple compounding frequencies
- Variable investment amounts and timing
- Adjustable investment duration
- Currency selection (USD, IDR, EUR)
- Theme preferences (light/dark mode)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is available as open source under the terms of the MIT License.

## Acknowledgments

- Data provided by Yahoo Finance
- Chart.js for visualization
- Tailwind CSS for styling
- yfinance library for financial data access