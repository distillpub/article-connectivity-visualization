
import tensorflow as tf

from python.dataset import AutoComplete
from python.model import PureGRU

tf.random.set_random_seed(450849059)  # From random.org
tf.logging.set_verbosity(tf.logging.INFO)

train_dataset = AutoComplete(repeat=True, batch_size=64)
valid_dataset = AutoComplete(repeat=True, dataset='valid', batch_size=64)
test_dataset = AutoComplete(repeat=False, dataset='test', batch_size=64)

model = PureGRU(train_dataset, name='autocomplete_gru_600',
                embedding_size=600,
                verbose=True)
model.train(max_steps=train_dataset.batches * 2, valid_dataset=valid_dataset)
