from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS  # Import pustaka CORS
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Configure Flask app to use public folder for static files
app = Flask(__name__, 
            static_folder='public',      
            static_url_path='/public',   
            template_folder='views')     

CORS(app)

@app.route('/')
def index():
    # Flask akan otomatis mencari 'index.html' di dalam folder 'views'
    return render_template('index.html')
@app.route('/api/tickers', methods=['GET'])
def get_tickers():
    """Endpoint to get a list of popular tickers"""
    try:
        # Return a predefined list of popular tickers
        popular_tickers = [
            # --- TOP 100 INDONESIA (IDX) ---
            {"symbol": "BBCA.JK", "name": "Bank Central Asia Tbk."},
            {"symbol": "BBRI.JK", "name": "Bank Rakyat Indonesia (Persero) Tbk."},
            {"symbol": "BMRI.JK", "name": "Bank Mandiri (Persero) Tbk."},
            {"symbol": "BBNI.JK", "name": "Bank Negara Indonesia (Persero) Tbk."},
            {"symbol": "TLKM.JK", "name": "Telkom Indonesia (Persero) Tbk."},
            {"symbol": "ASII.JK", "name": "Astra International Tbk."},
            {"symbol": "GOTO.JK", "name": "GoTo Gojek Tokopedia Tbk."},
            {"symbol": "AMMN.JK", "name": "Amman Mineral Internasional Tbk."},
            {"symbol": "TPIA.JK", "name": "Chandra Asri Pacific Tbk."},
            {"symbol": "UNVR.JK", "name": "Unilever Indonesia Tbk."},
            {"symbol": "ICBP.JK", "name": "Indofood CBP Sukses Makmur Tbk."},
            {"symbol": "INDF.JK", "name": "Indofood Sukses Makmur Tbk."},
            {"symbol": "ADRO.JK", "name": "Adaro Energy Indonesia Tbk."},
            {"symbol": "ANTM.JK", "name": "Aneka Tambang Tbk."},
            {"symbol": "PTBA.JK", "name": "Bukit Asam Tbk."},
            {"symbol": "ITMG.JK", "name": "Indo Tambangraya Megah Tbk."},
            {"symbol": "MDKA.JK", "name": "Merdeka Copper Gold Tbk."},
            {"symbol": "INCO.JK", "name": "Vale Indonesia Tbk."},
            {"symbol": "UNTR.JK", "name": "United Tractors Tbk."},
            {"symbol": "BRIS.JK", "name": "Bank Syariah Indonesia Tbk."},
            {"symbol": "ARTO.JK", "name": "Bank Jago Tbk."},
            {"symbol": "KLBF.JK", "name": "Kalbe Farma Tbk."},
            {"symbol": "MIKA.JK", "name": "Mitra Keluarga Karyasehat Tbk."},
            {"symbol": "HEAL.JK", "name": "Medikaloka Hermina Tbk."},
            {"symbol": "SILO.JK", "name": "Siloam International Hospitals Tbk."},
            {"symbol": "SMGR.JK", "name": "Semen Indonesia (Persero) Tbk."},
            {"symbol": "INTP.JK", "name": "Indocement Tunggal Prakarsa Tbk."},
            {"symbol": "CPIN.JK", "name": "Charoen Pokphand Indonesia Tbk."},
            {"symbol": "JPFA.JK", "name": "Japfa Comfeed Indonesia Tbk."},
            {"symbol": "AMRT.JK", "name": "Sumber Alfaria Trijaya Tbk."},
            {"symbol": "MAPI.JK", "name": "Mitra Adiperkasa Tbk."},
            {"symbol": "ACES.JK", "name": "Aspirasi Hidup Indonesia Tbk."},
            {"symbol": "ERAA.JK", "name": "Erajaya Swasembada Tbk."},
            {"symbol": "MYOR.JK", "name": "Mayora Indah Tbk."},
            {"symbol": "GGRM.JK", "name": "Gudang Garam Tbk."},
            {"symbol": "HMSP.JK", "name": "H.M. Sampoerna Tbk."},
            {"symbol": "ISAT.JK", "name": "Indosat Ooredoo Hutchison Tbk."},
            {"symbol": "EXCL.JK", "name": "XL Axiata Tbk."},
            {"symbol": "JSMR.JK", "name": "Jasa Marga (Persero) Tbk."},
            {"symbol": "PGAS.JK", "name": "Perusahaan Gas Negara Tbk."},
            {"symbol": "MEDC.JK", "name": "Medco Energi Internasional Tbk."},
            {"symbol": "AKRA.JK", "name": "AKR Corporindo Tbk."},
            {"symbol": "BSDE.JK", "name": "Bumi Serpong Damai Tbk."},
            {"symbol": "PWON.JK", "name": "Pakuwon Jati Tbk."},
            {"symbol": "CTRA.JK", "name": "Ciputra Development Tbk."},
            {"symbol": "SMRA.JK", "name": "Summarecon Agung Tbk."},
            {"symbol": "ASRI.JK", "name": "Alam Sutera Realty Tbk."},
            {"symbol": "BUKA.JK", "name": "Bukalapak.com Tbk."},
            {"symbol": "EMTK.JK", "name": "Elang Mahkota Teknologi Tbk."},
            {"symbol": "SCMA.JK", "name": "Surya Citra Media Tbk."},
            {"symbol": "BUMI.JK", "name": "Bumi Resources Tbk."},
            {"symbol": "BRMS.JK", "name": "Bumi Resources Minerals Tbk."},
            {"symbol": "HRUM.JK", "name": "Harum Energy Tbk."},
            {"symbol": "INDY.JK", "name": "Indika Energy Tbk."},
            {"symbol": "MBMA.JK", "name": "Merdeka Battery Materials Tbk."},
            {"symbol": "TOWR.JK", "name": "Sarana Menara Nusantara Tbk."},
            {"symbol": "TBIG.JK", "name": "Tower Bersama Infrastructure Tbk."},
            {"symbol": "BBTN.JK", "name": "Bank Tabungan Negara (Persero) Tbk."},
            {"symbol": "BDMN.JK", "name": "Bank Danamon Indonesia Tbk."},
            {"symbol": "BNGA.JK", "name": "Bank CIMB Niaga Tbk."},
            {"symbol": "PNBN.JK", "name": "Bank Pan Indonesia Tbk."},
            {"symbol": "BTPS.JK", "name": "Bank BTPN Syariah Tbk."},
            {"symbol": "SIDO.JK", "name": "Sido Muncul Tbk."},
            {"symbol": "WIKA.JK", "name": "Wijaya Karya (Persero) Tbk."},
            {"symbol": "PTPP.JK", "name": "PP (Persero) Tbk."},
            {"symbol": "ADHI.JK", "name": "Adhi Karya (Persero) Tbk."},
            {"symbol": "SMDR.JK", "name": "Samudera Indonesia Tbk."},
            {"symbol": "BIRD.JK", "name": "Blue Bird Tbk."},
            {"symbol": "SSIA.JK", "name": "Surya Semesta Internusa Tbk."},
            {"symbol": "LPPF.JK", "name": "Matahari Department Store Tbk."},
            {"symbol": "RALS.JK", "name": "Ramayana Lestari Sentosa Tbk."},
            {"symbol": "AUTO.JK", "name": "Astra Otoparts Tbk."},
            {"symbol": "SMSM.JK", "name": "Selamat Sempurna Tbk."},
            {"symbol": "IMAS.JK", "name": "Indomobil Sukses Internasional Tbk."},
            {"symbol": "ENRG.JK", "name": "Energi Mega Persada Tbk."},
            {"symbol": "ESSA.JK", "name": "Essa Kohuripan Tbk."},
            {"symbol": "DOID.JK", "name": "Delta Dunia Makmur Tbk."},
            {"symbol": "TCPI.JK", "name": "Transcoal Pacific Tbk."},
            {"symbol": "DSSA.JK", "name": "Dian Swastatika Sentosa Tbk."},
            {"symbol": "MAPA.JK", "name": "MAP Aktif Adiperkasa Tbk."},
            {"symbol": "BELI.JK", "name": "Global Digital Niaga Tbk. (Blibli)"},
            {"symbol": "WIIM.JK", "name": "Wismilak Inti Makmur Tbk."},
            {"symbol": "KAEF.JK", "name": "Kimia Farma Tbk."},
            {"symbol": "INAF.JK", "name": "Indofarma Tbk."},
            {"symbol": "ADMR.JK", "name": "Adaro Minerals Indonesia Tbk."},
            {"symbol": "MTEL.JK", "name": "Dayamitra Telekomunikasi Tbk."},
            {"symbol": "AVIA.JK", "name": "Avia Avian Tbk."},
            {"symbol": "CPRO.JK", "name": "Central Proteina Prima Tbk."},
            {"symbol": "MPMX.JK", "name": "Mitra Pinasthika Mustika Tbk."},
            {"symbol": "PANI.JK", "name": "Pantai Indah Kapuk Dua Tbk."},
            {"symbol": "BBYB.JK", "name": "Bank Neo Commerce Tbk."},
            {"symbol": "BABP.JK", "name": "Bank MNC Internasional Tbk."},
            {"symbol": "BVIC.JK", "name": "Bank Victoria International Tbk."},
            {"symbol": "DEWA.JK", "name": "Darma Henwa Tbk."},
            {"symbol": "ELSA.JK", "name": "Elnusa Tbk."},
            {"symbol": "RAJA.JK", "name": "Rukun Raharja Tbk."},
            {"symbol": "SIMP.JK", "name": "Salim Ivomas Pratama Tbk."},
            {"symbol": "LSIP.JK", "name": "PP London Sumatra Indonesia Tbk."},
            {"symbol": "AALI.JK", "name": "Astra Agro Lestari Tbk."},
            {"symbol": "SSMS.JK", "name": "Sawit Sumbermas Sarana Tbk."},

            # --- TOP 50 GLOBAL ASSETS (STOCKS, COMMODITIES, CRYPTO) ---
            {"symbol": "GC=F", "name": "Gold (Emas)"},
            {"symbol": "BTC-USD", "name": "Bitcoin"},
            {"symbol": "NVDA", "name": "NVIDIA Corporation"},
            {"symbol": "AAPL", "name": "Apple Inc."},
            {"symbol": "GOOGL", "name": "Alphabet Inc. (Google)"},
            {"symbol": "MSFT", "name": "Microsoft Corporation"},
            {"symbol": "AMZN", "name": "Amazon.com Inc."},
            {"symbol": "ETH-USD", "name": "Ethereum"},
            {"symbol": "META", "name": "Meta Platforms Inc."},
            {"symbol": "TSLA", "name": "Tesla Inc."},
            {"symbol": "AVGO", "name": "Broadcom Inc."},
            {"symbol": "2222.SR", "name": "Saudi Arabian Oil Co. (Aramco)"},
            {"symbol": "TSM", "name": "Taiwan Semiconductor Manufacturing (TSMC)"},
            {"symbol": "BRK-B", "name": "Berkshire Hathaway Inc."},
            {"symbol": "LLY", "name": "Eli Lilly and Company"},
            {"symbol": "WMT", "name": "Walmart Inc."},
            {"symbol": "JPM", "name": "JPMorgan Chase & Co."},
            {"symbol": "V", "name": "Visa Inc."},
            {"symbol": "TCEHY", "name": "Tencent Holdings Ltd."},
            {"symbol": "ORCL", "name": "Oracle Corporation"},
            {"symbol": "MA", "name": "Mastercard Incorporated"},
            {"symbol": "XOM", "name": "Exxon Mobil Corporation"},
            {"symbol": "005930.KS", "name": "Samsung Electronics"},
            {"symbol": "JNJ", "name": "Johnson & Johnson"},
            {"symbol": "PLTR", "name": "Palantir Technologies Inc."},
            {"symbol": "BAC", "name": "Bank of America Corp."},
            {"symbol": "ASML", "name": "ASML Holding N.V."},
            {"symbol": "ABBV", "name": "AbbVie Inc."},
            {"symbol": "NFLX", "name": "Netflix Inc."},
            {"symbol": "COST", "name": "Costco Wholesale Corp."},
            {"symbol": "MC.PA", "name": "LVMH Moet Hennessy Louis Vuitton"},
            {"symbol": "BABA", "name": "Alibaba Group Holding Ltd."},
            {"symbol": "AMD", "name": "Advanced Micro Devices Inc."},
            {"symbol": "HD", "name": "Home Depot Inc."},
            {"symbol": "PG", "name": "Procter & Gamble Co."},
            {"symbol": "KO", "name": "Coca-Cola Company"},
            {"symbol": "PEP", "name": "PepsiCo Inc."},
            {"symbol": "ADBE", "name": "Adobe Inc."},
            {"symbol": "SI=F", "name": "Silver (Perak)"},
            {"symbol": "NVS", "name": "Novartis AG"},
            {"symbol": "SHEL", "name": "Shell PLC"},
            {"symbol": "CVX", "name": "Chevron Corporation"},
            {"symbol": "RMS.PA", "name": "Hermes International"},
            {"symbol": "SAP", "name": "SAP SE"},
            {"symbol": "TM", "name": "Toyota Motor Corp."},
            {"symbol": "CSCO", "name": "Cisco Systems Inc."},
            {"symbol": "CRM", "name": "Salesforce Inc."},
            {"symbol": "MRK", "name": "Merck & Co. Inc."},
            {"symbol": "MCD", "name": "McDonald's Corporation"},
            {"symbol": "DIS", "name": "The Walt Disney Company"}
        ]
        return jsonify({"tickers": popular_tickers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/simulate', methods=['POST'])
def simulate():
    try:
        data = request.json
        ticker_symbol = data.get('ticker', 'AAPL').upper()
        initial_capital = float(data.get('initialCapital', 0))
        topup_amount = float(data.get('topupAmount', 0))
        start_year = int(data.get('startYear', datetime.now().year))
        end_year = int(data.get('endYear', start_year + 10))
        duration_years = end_year - start_year
        interval_per_year = int(data.get('interval', 12))

        # 1. Ambil data dari yfinance berdasarkan rentang tahun dari frontend
        asset = yf.Ticker(ticker_symbol)
        # Ambil history berdasarkan rentang tahun dari frontend (menyesuaikan dengan data historis yang tersedia)
        hist = asset.history(start=f"{start_year-10}-01-01", end=f"{end_year}-12-31")
        
        if hist.empty:
            return jsonify({"error": "Simbol tidak ditemukan di Yahoo Finance"}), 404

        # Check if 'Close' column exists in the DataFrame
        if 'Close' not in hist.columns:
            return jsonify({"error": "Tidak ada data penutupan (Close) tersedia untuk simbol ini"}), 404

        # 2. Hitung data historis tahunan untuk simulasi realistis
        # Konversi index menjadi datetime jika belum
        hist.index = pd.to_datetime(hist.index)

        # Set price_end and default cagr early to avoid undefined variable errors
        price_end = hist['Close'].iloc[-1]
        price_start = hist['Close'].iloc[0]
        actual_years = (hist.index[-1] - hist.index[0]).days / 365.25
        cagr = (price_end / price_start) ** (1 / actual_years) - 1  # Default CAGR

        # Ambil harga penutupan tahunan untuk menghitung return tahunan sebenarnya
        annual_data = hist.resample('YE').last()  # Ambil data akhir tiap tahun (using 'YE' instead of deprecated 'Y')
        if 'Close' in annual_data.columns:
            annual_returns = annual_data['Close'].pct_change().dropna()
        else:
            annual_returns = pd.Series(dtype=float)  # Empty series if no Close data

        # Jika kita tidak memiliki cukup data tahunan, gunakan data bulanan
        if len(annual_returns) < 2:
            monthly_data = hist.resample('ME').last()  # Using 'ME' instead of deprecated 'M'
            if 'Close' in monthly_data.columns:
                monthly_returns = monthly_data['Close'].pct_change().dropna()
            else:
                monthly_returns = pd.Series(dtype=float)  # Empty series if no Close data
            if len(monthly_returns) >= 12:  # Pastikan kita punya setidaknya 1 tahun data bulanan
                # Ambil 12 bulan terakhir untuk menghitung return bulanan rata-rata
                recent_returns = monthly_returns.tail(12)
                avg_monthly_return = recent_returns.mean()
                cagr = ((1 + avg_monthly_return) ** 12) - 1
            # else: # If not enough data, keep using the default CAGR which was already set
        else:
            # Gunakan rata-rata return tahunan historis
            cagr = annual_returns.mean()

        # Adjust the calculation based on interval frequency
        # For high frequency intervals (daily/weekly), we need to adjust the periodic rate calculation
        # to avoid precision issues
        if interval_per_year > 52:  # For daily or weekly intervals
            # Use a simple approach for high frequency compounding
            periodic_rate = cagr / interval_per_year
        else:
            # For monthly or less frequent intervals, use the compound rate formula
            periodic_rate = (1 + cagr) ** (1 / interval_per_year) - 1

        # 3. Logika Simulasi dengan siklus data historis (menggunakan pola tahunan historis)
        current_balance = initial_capital
        total_invested = initial_capital
        history = [{"year": 0, "balance": round(current_balance, 2), "invested": round(total_invested, 2)}]

        # Gunakan return historis tahunan secara siklus jika durasinya lebih panjang dari data historis
        historical_returns = annual_returns.values if len(annual_returns) >= 2 else [cagr]

        for y in range(1, duration_years + 1):
            # Pilih return berdasarkan siklus historis
            if y <= len(historical_returns):
                annual_return = historical_returns[y-1]
            else:
                # Jika tahun melebihi data historis, gunakan siklus dari awal
                annual_return = historical_returns[(y-1) % len(historical_returns)]

            # Adjust periodic rate calculation based on interval frequency
            if interval_per_year > 52:  # For daily or weekly intervals
                # Use a simple approach for high frequency compounding to avoid precision issues
                periodic_rate = annual_return / interval_per_year
            else:
                # For monthly or less frequent intervals, use the compound rate formula
                periodic_rate = (1 + annual_return) ** (1 / interval_per_year) - 1

            for i in range(interval_per_year):
                current_balance = (current_balance * (1 + periodic_rate)) + topup_amount
                total_invested += topup_amount

            # Ensure the balance doesn't go below a reasonable minimum (though it could be negative with extreme losses)
            history.append({
                "year": y,
                "balance": round(current_balance, 2),
                "invested": round(total_invested, 2)
            })

        # Ambil metadata aset
        asset_info = {
            "name": asset.info.get('longName', ticker_symbol),
            "cagr": round(cagr * 100, 2),
            "price": round(price_end, 2),
            "currency": asset.info.get('currency', 'USD'),
            "desc": asset.info.get('sector', 'N/A') + " - " + asset.info.get('industry', 'N/A')
        }

        return jsonify({
            "asset": asset_info,
            "history": history
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Jalankan server
    app.run(debug=True, port=5000)