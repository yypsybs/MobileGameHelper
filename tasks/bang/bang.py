from module.base.base import ModuleBase
from module.logger import logger


class Bang(ModuleBase):

    def run(self):
        logger.info('Bang start')
        self.device.swipe_vector()
        logger.info('Bang end')
        self.config.task_delay(server_update=True)
