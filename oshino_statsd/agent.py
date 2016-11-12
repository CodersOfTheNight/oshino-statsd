import asyncio
import multiprocessing as mp

from oshino import Agent
from oshino_statsd import receiver


class StatsdAgent(Agent):

    def __init__(self, cfg):
        super(StatsdAgent, self).__init__(cfg)
        self.queue = mp.Queue(maxsize=self.queue_size)

    def on_close(self):
        self.queue.close()
        self.queue.join_thread()

    def on_start(self):
        logger = self.get_logger()
        loop = asyncio.get_event_loop()
        self.proc = mp.Process(name="UDP server",
                               target=receiver.run,
                               args=(self.host, self.port, self.queue, logger))
        self.proc.daemon = True
        self.proc.start()

    @property
    def host(self):
        return self._data.get("host", "localhost")

    @property
    def port(self):
        return int(self._data.get("port", 8125))

    @property
    def queue_size(self):
        return int(self._data.get("queue-size", 1000))

    async def process(self, event_fn):
        loop = asyncio.get_event_loop()
        logger = self.get_logger()
        while not self.queue.empty():
            msg = self.queue.get()
            logger.debug("Got msg: {0}".format(msg))
