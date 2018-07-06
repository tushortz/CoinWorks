# create python3 virtual environment if not already created
# make sure to run in the parent directory as CoinWorks
python3 -m venv .env

# activate virtual environment
source .env/bin/activate

# install necessary modules if not already installed
pip install -r requirements.txt


# -----------------------------------------------------------------------------------
# run shuffling rnn
python python/shuffling/rnn.py

# run slided regression
# Format <python file> <bitcoin price> <occurrence matrix folder path> <save destination>
python python/bitcoin_prediction/sliding/slided_regression.py data/pricedBitcoin2009-2018.csv data/dailyOccmatrices results/sr_data.txt

# run random regression
python python/bitcoin_prediction/sliding/random_regression.py