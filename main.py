import logging
from cryptocomp.helpers import load_price_data, load_prediction_data
from cryptocomp.strategies import HoldingStrategy, NeuralStrategy, MaCrossoverStrategy, get_simple_entries_exits
import model.settings as settings

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logging.getLogger().setLevel(logging.INFO)

prediction = load_prediction_data(settings.bigboi, 199)
price = load_price_data('2021-04-09 UTC', '2021-10-24 UTC', 'ETH-USD', timeframe='daily')

entries, exits = get_simple_entries_exits(prediction, price)

logging.info("generating strategies")
hold = HoldingStrategy(price)
ma = MaCrossoverStrategy(price)
neural = NeuralStrategy(price, entries, exits)
logging.info("finished processing")

print(hold, ma, neural)
neural.portfolio.plot().show()
