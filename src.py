from module.alas import AzurLaneAutoScript


class AlasImplement(AzurLaneAutoScript):
    def restart(self):
        from tasks.base.app import App
        App(self.config, device=self.device).app_restart()

    def start(self):
        from tasks.base.app import App
        App(self.config, device=self.device).app_start()

    def goto_main(self):
        pass

    def daily_quest(self):
        from tasks.bang.bang import Bang
        Bang(self.config, device=self.device).run()


if __name__ == '__main__':
    src = AlasImplement('alas')
    src.loop()
